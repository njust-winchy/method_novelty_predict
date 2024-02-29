import numpy as np
import tokenizers

from Bi_interaction import Nov_model
from tqdm import tqdm
import torch.nn as nn
import os
import torch
import matplotlib.pyplot as plt
from read_data import getLoaders
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, classification_report
from sentence_transformers import SentenceTransformer
from transformers import *
from torch.nn.utils.rnn import pad_sequence


torch.cuda.set_device(0)
#tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
#tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
#tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
#tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
batch_size = 16

train_loader, val_loader = getLoaders(batch_size)

if torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
  print('No GPU available, using the CPU instead.')
  device = torch.device("cpu")

text_model = Nov_model()
text_model.to(device)
criterion = nn.CrossEntropyLoss()
no_decay = ['bias', 'LayerNorm.weight']
optimizer_grouped_parameters = [
    {'params': [p for n, p in text_model.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
    {'params': [p for n, p in text_model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.01}
]



optimizer = torch.optim.AdamW(optimizer_grouped_parameters, lr=1e-5)
#scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)  # 设定优优化器更新的时刻表

text_model.train()
result = []
EPOCH = 16
print("number of epoch = ", EPOCH)

loss_log1 = []
loss_log2 = []

train_f1_log = []

val_f1_log = []

train_acc_log = []
val_acc_log = []

final_output_train = []
final_output_val = []

best_val_out = []
max_acc = 0

for epoch in range(EPOCH):
    train_out = []
    train_true = []

    val_out = []
    val_true = []

    final_train_loss = 0.0
    final_val_loss = 0.0

    l1 = []
    l2 = []

    text_model.train()
    count = 0
    for data in tqdm(train_loader, desc="Train epoch {}/{}".format(epoch + 1, EPOCH)):
        sentence_s = data['input_s']
        sentence_b = data['input_b']
        token_s = tokenizer(sentence_s, padding=True, truncation=True, max_length=512, return_tensors="pt", add_special_tokens=True)['input_ids'].to(device)
        token_b = tokenizer(sentence_b, padding=True, truncation=True, max_length=512, return_tensors="pt", add_special_tokens=True)['input_ids'].to(device)
        att_s = tokenizer(sentence_s, padding=True, truncation=True, max_length=512, return_tensors="pt",
                            add_special_tokens=True)['attention_mask'].to(device)
        att_b = tokenizer(sentence_b, padding=True, truncation=True, max_length=512, return_tensors="pt",
                            add_special_tokens=True)['attention_mask'].to(device)
        padded_tensor = pad_sequence([token_s.T, token_b.T], batch_first=True, padding_value=0)
        input_s = padded_tensor[0]
        input_b = padded_tensor[1]
        padded_att_tensor = pad_sequence([att_s.T, att_b.T], batch_first=True, padding_value=0)
        input_att_s = padded_att_tensor[0]
        input_att_b = padded_att_tensor[1]
        #targets = data['nov_score'].to(device)
        targets = data['decision'].to(device)
        optimizer.zero_grad()
        pred = text_model(input_s.T, input_b.T, input_att_s.T, input_att_b.T)
        #pred = torch.argmax(pred).unsqueeze(1)
        _, out = torch.max(torch.softmax(pred, dim=1), dim=1)
        loss = criterion(pred, targets.long())
        train_out += out.tolist()
        train_true += targets.tolist()
        l1.append(loss.item())
        final_train_loss += loss.item()
        loss.requires_grad_(True)
        loss.backward()
        optimizer.step()
        #scheduler.step()

    loss_log1.append(np.average(l1))
    #scheduler.step()

    with torch.no_grad():
        text_model.eval()
        for data in tqdm(val_loader, desc="Valid epoch {}/{}".format(epoch + 1, EPOCH)):
            sentence_s = data['input_s']
            sentence_b = data['input_b']
            token_s = tokenizer(sentence_s, padding=True, truncation=True, max_length=512, return_tensors="pt",
                                add_special_tokens=True)['input_ids'].to(device)
            token_b = tokenizer(sentence_b, padding=True, truncation=True, max_length=512, return_tensors="pt",
                                add_special_tokens=True)['input_ids'].to(device)
            att_s = tokenizer(sentence_s, padding=True, truncation=True, max_length=512, return_tensors="pt",
                              add_special_tokens=True)['attention_mask'].to(device)
            att_b = tokenizer(sentence_b, padding=True, truncation=True, max_length=512, return_tensors="pt",
                              add_special_tokens=True)['attention_mask'].to(device)
            padded_tensor = pad_sequence([token_s.T, token_b.T], batch_first=True, padding_value=0)
            input_s = padded_tensor[0]
            input_b = padded_tensor[1]
            padded_att_tensor = pad_sequence([att_s.T, att_b.T], batch_first=True, padding_value=0)
            input_att_s = padded_att_tensor[0]
            input_att_b = padded_att_tensor[1]
            #targets = data['nov_score'].to(device)
            targets = data['decision'].to(device)
            pred_val = text_model(input_s.T, input_b.T, input_att_s.T, input_att_b.T)
            _, out_val = torch.max(torch.softmax(pred_val, dim=1), dim=1)

            loss = criterion(pred_val, targets.long())
            loss.requires_grad_(True)
            val_out += out_val.tolist()
            val_true += targets.tolist()
            l2.append(loss.item())
            l2.append(loss.item())

            final_val_loss += loss.item()

        # scheduler.step(final_val_loss)
        loss_log2.append(np.average(l2))
        curr_lr = optimizer.param_groups[0]['lr']

    train_out = np.array(train_out)
    train_true = np.array(train_true)

    val_out = np.array(val_out)
    val_true = np.array(val_true)

    print("Epoch {}, loss: {}, val_loss: {}".format(epoch + 1, final_train_loss / len(train_loader),
                                                    final_val_loss / len(val_loader)))
    print(
        f"TRAINING F1 SCORE: {f1_score(train_true, train_out, average='weighted')} \nValidation F1 SCORE: {f1_score(val_true, val_out, average='weighted')}")
    print(
        f"TRAINING ACCURACY: {accuracy_score(train_true, train_out)} \nValidation ACCURACY: {accuracy_score(val_true, val_out)}")

    train_f1_log.append(f1_score(train_true, train_out, average='weighted'))
    val_f1_log.append(f1_score(val_true, val_out, average='weighted'))

    train_acc_log.append(accuracy_score(train_true, train_out))
    val_acc_log.append(accuracy_score(val_true, val_out))

    if (accuracy_score(val_true, val_out) > max_acc):
        torch.save(text_model.state_dict(), "scibert_model.pt")
        max_acc = accuracy_score(val_true, val_out)
        best_val_out = val_out

plt.plot(range(len(loss_log1)), loss_log1)
plt.plot(range(len(loss_log2)), loss_log2)
plt.savefig('loss_curve.png')
print("MAXIMUM ACCURACY:", max_acc)

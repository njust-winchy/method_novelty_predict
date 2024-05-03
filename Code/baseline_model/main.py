import numpy as np
import tokenizers
import torch.nn.functional as F
from model import Nov_model
from tqdm import tqdm
import torch.nn as nn
import os
import torch
import matplotlib.pyplot as plt
from split_data import getLoaders
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, classification_report
from transformers import *

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
#tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
#tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
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

#scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)  #Set the schedule for optimizer updates



text_model.train()
result = []
EPOCH = 12
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
        sentence = data['input']

        input_ = tokenizer(sentence, padding=True, truncation=True, max_length=512, return_tensors="pt", add_special_tokens=True)['input_ids'].to(device)
        #input_ids = tokenizer.encode(sentence, add_special_tokens=True, max_length=512, truncation=True, pad_to_max_length=True, return_tensors="pt").to(device)
        #targets = data['nov_score'].to(device)
        targets = data['decision'].to(device)
        optimizer.zero_grad()
        pred = text_model(input_)
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
    text_model.eval()
    with torch.no_grad():

        for data in tqdm(val_loader, desc="Valid epoch {}/{}".format(epoch + 1, EPOCH)):
            sentence = data['input']
            input_ = tokenizer(sentence, padding=True, truncation=True, max_length=512, return_tensors="pt",
                               add_special_tokens=True)['input_ids'].to(device)

            #targets = data['nov_score'].to(device)
            targets = data['decision'].to(device)
            pred_val = text_model(input_)
            _, out_val = torch.max(torch.softmax(pred_val, dim=1), dim=1)

            #fin_res = torch.argmax(pred).reshape(1)
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
        torch.save(text_model.state_dict(), "bert_model.pt")
        max_acc = accuracy_score(val_true, val_out)
        best_val_out = val_out

plt.plot(range(len(loss_log1)), loss_log1)
plt.plot(range(len(loss_log2)), loss_log2)
plt.savefig('loss_curve.png')
print("MAXIMUM ACCURACY:", max_acc)

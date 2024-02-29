import json

import torch
from Bi_interaction import Nov_model
from read_data import gettestLoaders
from tqdm.autonotebook import tqdm
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, classification_report
from transformers import *
from torch.nn.utils.rnn import pad_sequence
import numpy as np
device = torch.device("cuda:0")

batch_size = 16
model = Nov_model().to(device)
model.load_state_dict(torch.load('E:\wwq\proposed_model\\scibert_model.pt'))

#tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
#tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
#tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
#tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
test_loader = gettestLoaders(batch_size)
test_out = []
test_true = []
result = []
m = 0
for data in tqdm(test_loader, desc="test"):
    sentence_s = data['input_s']
    sentence_b = data['input_b']
    token_s = \
    tokenizer(sentence_s, padding=True, truncation=True, max_length=512, return_tensors="pt", add_special_tokens=True)[
        'input_ids'].to(device)
    token_b = \
    tokenizer(sentence_b, padding=True, truncation=True, max_length=512, return_tensors="pt", add_special_tokens=True)[
        'input_ids'].to(device)
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
    pred = model(input_s.T, input_b.T, input_att_s.T, input_att_b.T)
    _, out = torch.max(torch.softmax(pred, dim=1), dim=1)

    test_out += out.tolist()
    test_true += targets.tolist()
print(f"test F1 SCORE: {f1_score(test_true, test_out, average='weighted')} \ntest ACCURACY: {accuracy_score(test_true, test_out)}")










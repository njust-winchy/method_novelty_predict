import json

import torch
from model import Nov_model
#from split_data import gettestLoaders
from load_method import gettestLoaders
from tqdm.autonotebook import tqdm
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, classification_report
from transformers import *
import numpy as np
device = torch.device("cuda:0")

batch_size = 16
model = Nov_model()
model.load_state_dict(torch.load('bert_model.pt'))

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
#tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
#tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
#tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
#tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
test_loader = gettestLoaders(batch_size)
test_out = []
test_true = []
result = []
m = 0
for data in tqdm(test_loader, desc="test"):
    sentence = data['input']
    input_ = tokenizer(sentence, padding=True, truncation=True, max_length=512, return_tensors="pt", add_special_tokens=True)[
        'input_ids'].to(device)
    #targets = data['nov_score'].to(device)
    targets = data['decision'].to(device)
    pred = model(input_)
    _, out = torch.max(torch.softmax(pred, dim=1), dim=1)

    test_out += out.tolist()
    test_true += targets.tolist()
print(f"test F1 SCORE: {f1_score(test_true, test_out, average='weighted')} \ntest ACCURACY: {accuracy_score(test_true, test_out)}")










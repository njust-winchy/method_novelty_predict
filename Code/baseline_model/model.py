import numpy as np
import os
import torch
import torch.nn as nn
from transformers import *

# 全局变量
RANDOM_SEED = 400
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
class Nov_model(nn.Module):
    def __init__(self):
        n_classes = 3
        super(Nov_model, self).__init__()

        self.model = BertModel.from_pretrained('bert-base-uncased').to(device)
        #self.model = RobertaModel.from_pretrained('roberta-base').to(device)
        #self.model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased').to(device)
        #self.model = AlbertModel.from_pretrained('albert-base-v2').to(device)
        #self.model = XLNetModel.from_pretrained('xlnet-base-cased').to(device)
        self.linear = nn.Linear(768, n_classes).to(device)

        self.dropout = nn.Dropout(0.2)
    def forward(self, sentence):
        #pro_sentence = self.sentence_encode(sentence)
        last_hidden_state = self.model(sentence).last_hidden_state
        input_sentence = last_hidden_state[:, 0, :]
        output = self.dropout(self.linear(input_sentence))
        return output
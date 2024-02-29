import numpy as np

import os
import torch
import torch.nn as nn
from transformers import *
import math
import torch.nn.functional as F

# 全局变量
RANDOM_SEED = 400
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
class Nov_model(nn.Module):
    def __init__(self):
        n_classes = 2
        super(Nov_model, self).__init__()
        self.model = BertModel.from_pretrained('bert-base-uncased').to(device)
        #self.model = RobertaModel.from_pretrained('roberta-base').to(device)
        #self.model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased').to(device)
        #self.model = AlbertModel.from_pretrained('albert-base-v2').to(device)
        #self.model = XLNetModel.from_pretrained('xlnet-base-cased').to(device)
        self.sparse_att = SparseAttention(768, 6, 128)
        self.self_att = SelfAttention(768, 12)
        self.FFN = FeedForwardNetwork(768, 512, 128, 1)
        self.att_re = SelfAttentionReduction(128)
        self.dropout = nn.Dropout(0.2)
        self.FC_layer = FullyConnectedLayer(128, n_classes)
    def forward(self, sentence_s, sentence_b, att_s, att_b):
        sen_s = self.model(sentence_s, attention_mask = att_s).last_hidden_state
        sen_b = self.model(sentence_b, attention_mask = att_b).last_hidden_state
        sentence_bb = self.self_att(sen_b)
        att_ss = self.sparse_att(sen_s, sentence_bb)
        #bi_output = self.dropout(self.FFN(att_ss))
        bi_output = self.dropout(self.FFN(att_ss))
        att_output = self.att_re(bi_output)
        output = self.FC_layer(att_output)
        return output


class SparseAttention(nn.Module):
    def __init__(self, input_dim, num_heads, sparse_dim):
        super(SparseAttention, self).__init__()
        self.num_heads = num_heads
        self.head_dim = input_dim // num_heads
        self.sparse_dim = sparse_dim

        # 注意力权重参数
        self.q_linear = nn.Linear(input_dim, input_dim)
        self.kv_linear = nn.Linear(input_dim, 2*input_dim)
        self.fc_out = nn.Linear(input_dim, input_dim)

    def forward(self, x, y):
        b, t, _ = x.size()
        m, n, _ = y.size()
        # 计算注意力权重
        q = self.q_linear(x).view(b, t, 1, self.num_heads, self.head_dim).permute(2, 0, 3, 1, 4)
        kv = self.kv_linear(y).view(m, n, 2, self.num_heads, self.head_dim).permute(2, 0, 3, 1, 4)
        k = kv[0]
        v = kv[1]
        attn_weights = torch.matmul(q[0], k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        # 选择部分位置进行注意力
        attn_weights = F.softmax(attn_weights[:, :, :self.sparse_dim, :self.sparse_dim], dim=-1)
        # 注意力加权求和
        attn_output = torch.matmul(v, attn_weights)
        attn_output = attn_output.permute(0, 2, 1, 3).contiguous().view(-1, n, 768)

        # 线性变换和残差连接
        output = self.fc_out(attn_output) + y
        return output



class FeedForwardNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers, activation=nn.ReLU()):
        super(FeedForwardNetwork, self).__init__()
        layers = []

        # 输入层到隐藏层
        layers.append(nn.Linear(input_dim, hidden_dim))
        layers.append(activation)

        # 隐藏层到隐藏层
        for _ in range(num_layers - 1):
            layers.append(nn.Linear(hidden_dim, hidden_dim))
            layers.append(activation)

        # 隐藏层到输出层
        layers.append(nn.Linear(hidden_dim, output_dim))

        # 构建前馈神经网络
        self.ffn = nn.Sequential(*layers)

    def forward(self, x):
        return self.ffn(x)


class SelfAttention(nn.Module):
    def __init__(self, input_dim, num_heads):
        super(SelfAttention, self).__init__()
        self.input_dim = input_dim
        self.num_heads = num_heads
        self.head_dim = input_dim // num_heads

        # 注意力权重参数
        self.qkv_linear = nn.Linear(input_dim, 3 * input_dim)

    def forward(self, x):
        b, t, _ = x.size()

        # 计算注意力权重
        qkv = self.qkv_linear(x).view(b, t, 3, self.num_heads, self.head_dim).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]

        attn_weights = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)

        # 使用 softmax 计算注意力权重
        attn_weights = F.softmax(attn_weights, dim=-1)

        # 注意力加权求和
        attn_output = torch.matmul(attn_weights, v)
        attn_output = attn_output.permute(0, 2, 1, 3).contiguous().view(b, t, -1)

        return attn_output

class SelfAttentionReduction(torch.nn.Module):
    def __init__(self, input_dim):
        super(SelfAttentionReduction, self).__init__()
        self.input_dim = input_dim
        self.attention_weights = torch.nn.Linear(input_dim, 1)

    def forward(self, x):
        # 计算注意力权重
        attn_weights = F.softmax(self.attention_weights(x), dim=1)

        # 加权平均
        reduced_representation = torch.sum(attn_weights * x, dim=1)

        return reduced_representation

class FullyConnectedLayer(nn.Module):
    def __init__(self, input_size, output_size):
        super(FullyConnectedLayer, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, x):
        # 输入 x 的形状应为 (batch_size, input_size)
        output = self.fc(x)
        return output
import torch
import numpy as np
import os
from util import preprocess_text
from torch.utils.data import Dataset, DataLoader, SubsetRandomSampler
from nltk.tokenize import sent_tokenize, word_tokenize
from tqdm import tqdm
import json

#batch_size = 16
class Data(Dataset):
    def __init__(self, rev_sentence, chat_review, labels):
        self.rev_sentence = rev_sentence
        self.chat_review = chat_review
        self.label = labels
        self.max_len = 50


    @classmethod

    def getReader(self):
        with open('Dataset.json') as f:
            datasets = json.load(f)
        nov_dataset = []
        for t in tqdm(datasets):
            preprocess_dir = {}
            s = t['novelty_sentence']
            b = t['chat_content']
            #preprocess_dir['raw_sentence'] = s
            input_s = preprocess_text(s)
            input_b = preprocess_text(b)

            preprocess_dir['input_s'] = input_s
            preprocess_dir['input_b'] = input_b
            #preprocess_dir['nov_sentence'] = process_s
            #preprocess_dir['chat_review'] = process_b
            nov = torch.zeros(1)
            if t['novelty_score'] <= 2:
                label = 0
            else:
                label = 1
            nov[0] = label
            if t['decision'] == 2:
                continue
            dec = torch.zeros(1)
            dec[0] = t['decision']
            preprocess_dir['decision'] = dec[0]
            preprocess_dir['nov_score'] = nov[0]
            nov_dataset.append(preprocess_dir)



        train_size = int(0.8 * len(nov_dataset))
        val_size = int(0.1 * len(nov_dataset))
        test_size = len(nov_dataset) - train_size - val_size

        train_dataset, val_dataset, test_dataset = torch.utils.data.random_split(nov_dataset, [train_size, val_size, test_size])

        return train_dataset, val_dataset, test_dataset

def getLoaders(batch_size):
    print('Reading the training Dataset...')

    train_dataset, val_dataset, test_dataset = Data.getReader()
    #test_dataset, train_dataset, val_dataset = Data.getReader()
    print('Reading the validation Dataset...')
    #print()

    trainloader = DataLoader(dataset=train_dataset, batch_size=batch_size, num_workers=0, shuffle=True)
    validloader = DataLoader(dataset=val_dataset, batch_size=batch_size, num_workers=0, shuffle=True)
    return trainloader, validloader
def gettestLoaders(batch_size):

    _, _, test_dataset = Data.getReader()
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, num_workers=0, shuffle=True)

    return test_loader
#a = getLoaders(16)
#b = gettestLoaders(16)


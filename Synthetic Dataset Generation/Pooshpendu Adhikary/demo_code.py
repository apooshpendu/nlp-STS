#!/usr/bin/env python
import os
import sys
import spacy
import pattern.en
import nlpaug.augmenter.word as naw
import pandas as pd
from pass2act import pass2act
from nlpaug.util import Action
from random import randint

class SyntheticDataGenerator:
    
    def __init__(self):
        antAug = naw.AntonymAug();
        synAug = naw.SynonymAug(aug_src='wordnet');
        embAug = naw.ContextualWordEmbsAug(
            model_path='bert-base-uncased', action="substitute");
            
        self.model_dict = { 0: antAug,
                        1: synAug, 2: embAug};
                        
        self.output_data = { 'Sentence1': [],
                        'Sentence2': [], 'Label': [] };
                        
    def create_synthetic_data(self, input_tsv_file):
        print("Reading from the input file {0}".format(input_tsv_file));
        input_data = pd.read_csv("dev_2k.tsv", sep="\t", error_bad_lines=False);
        for _,row in input_data.iterrows():
            origText = row[1];
            _model = randint(0,2);
            aug = model_dict[_model];
            augText = aug.augment(origText);
            score = 1 if _model == 1 else 0;
            output_data["Sentence1"].append(origText);
            output_data["Sentence2"].append(augText);
            output_data["Label"].append(score);
            count += 1;
            total += 1;
            if count >= 200:
                print("{0} sentences created".format(total));
                dump_data_to_file(output_data, "synthetic_data.csv");
                output_data = { 'Sentence1': [],
                            'Sentence2': [], 'Label': [] };
                count = 0;
    
    def dump_data_to_file(self, pandasDict, filePath):
        df = pd.DataFrame(pandasDict);
        df.to_csv(filePath, mode='a', header=False);


model_dict = {
    0: antAug,
    1: synAug,
    2: embAug};
#text = 'The quick brown fox jumps over the lazy dog.'
#print("Original text: ", text);
#print(model_dict[1]);
#for i in range(5):
#    _id = randint(0,2)
#    aug = model_dict[_id]
#    text = aug.augment(text);
#    print(str(_id), "Formatted text: ", text);
    
print("Reading from the input file");
input_data = pd.read_csv("dev_2k.tsv", sep="\t", error_bad_lines=False);
# print(input_data.head(10));

output_data = {'Sentence1': [],
        'Sentence2': [],
        'Label': []
        };

score = 0;
count = 0;
total = 0;

def create_synthetic_data(self, input_tsv_file):
    print("Reading from the input file {0}".format(input_tsv_file));
    input_data = pd.read_csv("dev_2k.tsv", sep="\t", error_bad_lines=False);
    for _,row in input_data.iterrows():
        origText = row[1];
        _model = randint(0,2);
        aug = model_dict[_model];
        augText = aug.augment(origText);
        score = 1 if _model == 1 else 0;
        output_data["Sentence1"].append(origText);
        output_data["Sentence2"].append(augText);
        output_data["Label"].append(score);
        count += 1;
        total += 1;
        if count >= 200:
            print("{0} sentences created".format(total));
            dump_data_to_file(output_data, "synthetic_data.csv");
            output_data = {'Sentence1': [],
                'Sentence2': [],
                'Label': []
                };
            count = 0;
    
def dump_data_to_file(self, pandasDict, filePath):
    df = pd.DataFrame(pandasDict);
    df.to_csv(filePath, mode='a', header=False);


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
    
    def __init__(self, input_file, output_file):
    
        self.input_file = input_file;
        self.output_file = output_file;
        
        antAug = naw.AntonymAug();
        synAug = naw.SynonymAug(aug_src='wordnet');
        embAug = naw.ContextualWordEmbsAug(
            model_path='bert-base-uncased', action="substitute");
            
        self.model_dict = { 0: antAug,
                        1: synAug, 2: embAug};
                        
        self.output_data = { 'Sentence1': [],
                        'Sentence2': [], 'Label': [] };
                        
    def create_synthetic_data(self):
        
        augScore = 0;
        currCount = 0;
        totalCount = 0;
        print("Reading from the input file {0}".format(self.input_file));
        input_data = pd.read_csv(self.input_file, sep="\t", error_bad_lines=False);
        for _,row in input_data.iterrows():
            origText = row[1].strip();
            _model = randint(0,2);
            aug = self.model_dict[_model];
            augText = aug.augment(origText);
            augScore = 1 if _model == 1 else 0;
            self.output_data["Sentence1"].append(origText);
            self.output_data["Sentence2"].append(augText);
            self.output_data["Label"].append(augScore);
            currCount += 1;
            totalCount += 1;
            if currCount >= 200:
                print("{0} sentences created".format(totalCount));
                self.dump_data_to_file(self.output_data);
                self.output_data = { 'Sentence1': [],
                            'Sentence2': [], 'Label': [] };
                currCount = 0;
        
        print("Data generation complete");
    
    def dump_data_to_file(self, pandasDict):
        df = pd.DataFrame(pandasDict);
        df.to_csv(self.output_file, mode='a', header=False);
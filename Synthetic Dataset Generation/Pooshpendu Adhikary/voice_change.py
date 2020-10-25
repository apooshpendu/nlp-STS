#!/usr/bin/env python
import sys
import spacy
import pattern.en
from pass2act import pass2act

nlp = spacy.load('en')
prev = ''
acts = ''

with open("input_file.txt", "r") as file:
    with open("output_file.txt", "w") as out:
        for l in file:
            s = l.strip();
            if s == '':
                continue;
            else:
                prev = s;
                acts = pass2act(s);
                print(acts, file=out);
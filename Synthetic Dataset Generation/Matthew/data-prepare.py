import csv
from googletrans import Translator
import pandas as pd
import nltk
import re
from nltk.corpus import wordnet
from random import randrange
from random import choice

def get_synonym(word):
    # get the first synonym we can find
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            if word.lower() != lemma.name().lower():
                return str(lemma.name().replace("_", " "))
    # if all else fails, return the original word
    return word



def is_word(word):
    if re.match(r"^[.,!?; ]+$", word):
        return False
    else:
        return True



def augment_sentence(text, num=1):
    # take an input sentence and augment a certain number of words to be their synonym
    # first, split out all the words from the punctuation (spaces, commas, etc.)
    aug_text = re.findall(r"[\w']+|[.,!?; ]", text)

    # get the indexes of real words that we can choose from (not allowing spaces or punctuation)
    indices = []
    for i, word in enumerate(aug_text):
        if is_word(word):
            indices.append(i)

    # choose n words and augment them
    for i in range(num):
        index = choice(indices)
        aug_text[index] = get_synonym(aug_text[index])

    return ''.join(aug_text)


# the goal is to have many languages that are as different as possible
languages = ["ja", "af", "he", "la", "haw", "vi", "zu", "es"]
translator = Translator()

def translate_sentence(text, num=1):
    assert num <= 8

    trans = translator.translate(text, dest="de")  # first translation is to german
    # further translations use the language list
    for i in range(num):
        trans = translator.translate(trans.text, dest=languages[i])

    y = translator.translate(trans.text, dest='en')
    # print(dataset[385])
    # print(y.text)

    return y.text







dataset = []

with open("sts-train.csv", encoding="utf8") as infile:
    reader = csv.reader(infile, delimiter='\t')
    i = 0
    for row in reader:
        # sts sentences are found on indexes 5 and 6
        # these sentences are often similar, so we will only use index 5
        dataset.append(row[5])


# dataset size is 5711
# print(len(dataset))





## begin translating



output_data = pd.DataFrame(columns = ['Sentence1', 'Sentence2', 'Gold Label', 'is_sts'])

# output_data = output_data.append({'Sentence1' : 'Ankit', 'Sentence2' : 97, 'Gold Label' : 2200, 'is_sts' : 2200}, ignore_index = True)





j = 25
for i, text in enumerate(dataset):
    # trans = translator.translate(dataset[385], dest="de") # first translation is to german
    # for i in range(1):
    #     trans = translator.translate(trans.text, dest=languages[i])
    #
    # y = translator.translate(trans.text, dest='en')
    # output = text
    # print(dataset[385])
    # print(y.text)

    # make 5 sentence pairs, one for each level of change (other than 0)

    # similarity 5
    output = translate_sentence(text, 1)
    output_data = output_data.append({'Sentence1': text, 'Sentence2': output, 'Gold Label': 5, 'is_sts': "true"},
                                     ignore_index=True)

    # similarity 4
    output = augment_sentence(translate_sentence(text, 2), 2)
    output_data = output_data.append({'Sentence1': text, 'Sentence2': output, 'Gold Label': 4, 'is_sts': "true"},
                                     ignore_index=True)

    # similarity 3
    output = augment_sentence(translate_sentence(text, 3), 3)
    output_data = output_data.append({'Sentence1': text, 'Sentence2': output, 'Gold Label': 3, 'is_sts': "true"},
                                     ignore_index=True)

    # similarity 2
    output = augment_sentence(translate_sentence(text, 4), 3)
    output_data = output_data.append({'Sentence1': text, 'Sentence2': output, 'Gold Label': 2, 'is_sts': "true"},
                                     ignore_index=True)

    # similarity 1
    output = augment_sentence(translate_sentence(text, 4), 4)
    output_data = output_data.append({'Sentence1': text, 'Sentence2': output, 'Gold Label': 1, 'is_sts': "true"},
                                     ignore_index=True)

    if i == j:
        j += 25
        output_data.to_csv("output.csv", sep='\t')
        print("saving work (25 done)")



output_data.to_csv("output.csv", sep='\t')






# x = translator.translate(dataset[0], dest='ja') # translate to japanese
# print(x.text)
#
#
# x = translator.translate(x.text, dest='la') # translate to
# print(x.text)
#
#
#
#
# y = translator.translate(x.text, dest='en')
# print(y.text)
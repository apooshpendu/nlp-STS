#!/usr/bin/env python
# coding: utf-8

# In[57]:

import sys
import nltk
import googletrans
import pybacktrans
from pybacktrans import BackTranslator
import pandas as pd
import random
import requests
from langdetect import detect


url = 'http://qim.fs.quoracdn.net/quora_duplicate_questions.tsv'
r = requests.get(url, allow_redirects=True)
open('input_quora_data.tsv', 'wb').write(r.content)

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}
lang = set(LANGUAGES.keys())
lang.remove('en')
lang.remove('ug')
lang.remove('or')
# In[32]:


translator = BackTranslator()


# In[33]:


def backt(sentence, mid_lang):
    result = translator.backtranslate(sentence, src = 'en', mid = mid_lang)
    return result.text


# In[48]:


def get_lang(lang):
    return random.choice(tuple(lang))


# In[29]:


data = pd.read_csv('input_quora_data.tsv', sep='\t')


# In[30]:


# In[38]:


data = data.dropna()


# In[64]:

def gen_data(num_line):
    sent1, sent2 = [], []
    for _, row in data.iterrows():
        if len(sent1) >= num_line:
            break
        if row.is_duplicate == 1:
            try:
                lang1, lang2 = get_lang(lang), get_lang(lang)
                ques1 = row.question1
                if detect(ques1) != 'en':
                    continue
                new_q1, new_q2 = backt(ques1, lang1), backt(ques1, lang2)
                if detect(new_q1) != 'en' or detect(new_q2) != 'en':
                    continue
                sent1.append(new_q1)
                sent2.append(new_q2)
            except Exception as e:
                print(e)
    return sent1, sent2


# In[82]:


new_pd = pd.DataFrame()
sent1, sent2 = gen_data(int(sys.argv[1]))
label = [1] * len(sent1)
new_pd['Sentence1'] = sent1
new_pd['Sentence2'] = sent2
new_pd['Gold Label'] = label
new_pd['is_sts'] = ['No'] * len(sent1)

new_pd.to_csv('paraphrase.csv')





# In[88]:









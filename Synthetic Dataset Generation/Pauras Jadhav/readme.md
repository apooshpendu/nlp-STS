## How to generate Synthetic Data ##
1. Open *create_dataset.py*.
2. Change the link to the original data
3. Run the script using Python command prompt.

### Requirements ###
1. Python 3.6.
2. Libraries: spacy, pattern, numpy, requests, nlpaug, nltk

### Installation ###
1. pip install -U spacy
2. python -m spacy download en
3. pip install numpy requests nlpaug
4. pip install nltk>=3.4.5
5. pip install torch>=1.6.0 -f https://download.pytorch.org/whl/torch_stable.html
6. pip install transformers>=3.0.2

### Note ###
If BERT model is not loaded, it take some time executing the script for the first time.

### Reference ###
DanManN passive to active
https://github.com/DanManN/pass2act

makcedward nlpaug
https://github.com/makcedward/nlpaug

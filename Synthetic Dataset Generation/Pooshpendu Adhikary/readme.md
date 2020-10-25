## How to generate Synthetic Data ##
1. Open *create_dataset.py*.
2. Change the parameters for the input file and output file.
3. Run the script using Python command prompt.

### Requirements ###
1. Python 3.6.
2. Libraries: spacy, pattern, numpy, requests, nlpaug, nltk, pandas

### Installation ###
1. pip install -U spacy
2. python -m spacy download en
3. pip install numpy requests nlpaug
4. pip install nltk>=3.4.5
5. pip install torch>=1.6.0 -f https://download.pytorch.org/whl/torch_stable.html
6. pip install transformers>=3.0.2

### Description ###
It uses passive-to-active voice conversion and word swapping techniques using BERT and WordNet to create synthetic data. For generating dataset, PAWS dataset's partial data has been used as in input. The result is a csv file where each row contains original as well as generated sentence, similarity level and flag indicating whether it can be used for STS.

### Note ###
If BERT model is not loaded, it take some time executing the script for the first time.

### Reference ###
DanManN passive to active
https://github.com/DanManN/pass2act

makcedward nlpaug
https://github.com/makcedward/nlpaug

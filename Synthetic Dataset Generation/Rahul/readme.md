## How to generate Synthetic Data ##
1. Open *syn_ant_paraphraser.py*.
2. Make sure the input and output file paths are configured properly.
3. Open terminal/cmd and run python syn_ant_paraphraser.py arg
4. Where arg=number of paraphrases you want in output file.
5. Output file will be generated in the same location with name syn_ant.csv

### Requirements ###
1. Python 3.6 or higher
2. Libraries: Pandas, csv, nltk, json, nltk.stopwords, nltk.punkt, nltk.wordnet, nltk.averaged_perceptron_tagger

### Installation ###
1. pip install pandas
2. pip install nltk>=3.4.5
3.nltk.download("wordnet")

### Contribution ###
1. The script uses the Microsoft Research Paraphrase Corpus (MRPC) as input dataset. The dataset is filtered and only the raw sentences are extracted.
2. The extracted sentences are tokenized and stop words are removed.
3. The wordnet nltk corpus is used for getting the synonyms and antonym words.
4. The script would identify the adjectives and adverbs(JJ & RB) from the input sentences and the respective words are replaced with their synonyms and antonyms obtained from     wordnet.
5. Gold Label is assigned for synonyms and antonym paraphrases as 1 and 0 respectively.
6. The generateDataset function in the script is used for generating the specified number of sentences in the output file.

### Note ###
The script takes atmost 5 mins to run. You can also visit the ipython notebooks provided by google colab to try the code.
https://colab.research.google.com/drive/1FoaU_7MRlQjjYsIuk3qxGsxnvoyqf1Ut.

### Reference ###

Microsoft Research Paraphrase Corpus

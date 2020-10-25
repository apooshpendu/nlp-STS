## How to generate Synthetic Data ##
1. Open *gen_pd.py*.
2. Change the link to the original data
3. Run the script using Python command prompt `python gen_pd.py num_pairs` with the number of pairs to be generated as an argument

### Requirements ###
1. Python 3.6.
2. Libraries: nltk, googletrans, pybacktrans, pandas, langdetect

### Installation ###
1. pip install nltk>=3.4.5
2. pip install googletrans
3. pip install pybacktrans
4. pip install pandas
5. pip install langdetect

### Note ###
Backtranslation takes some time to generate the data

### Contribution ###
Used the **Quora Question Pair** dataset as input data.
The dataset has a pair of question with a label, 1 for similar questions and 0 for different.
Used two different languages for backtranslating the similar pairs (both questions were backtranslated using different language). Used the **pybacktrans** library for backtranslation.
The choice of language for backtranslation is random from the list of supported languages in the **googletrans API**.
Some of the original data was in languages other than in English. Used the **Langdetect** library to detect non-English languages and discard them.

### Reference ###
*Python library for [backtranslation](https://github.com/monologg/py-backtrans) (with Google Translate)

*[Googletrans](https://pypi.org/project/py-googletrans/)

*[Langdetect](https://pypi.org/project/langdetect/)

# Semantic Textual Similarity
Group Project of **CSE 576 : Natural Language Processing** at ASU

## Overview
The task is to generate synthetic dataset from existing datasets by applying various methods. This way we will generate new dataset to manage data scarcity and will be able to add some variations in the dataset to train an NLP model for better accuracy. Instead of using single method, we will utilize various algorithms such as word substitution and translation of sentences to generate our synthetic data.
1. _Stack Exchange data explorer_ - stackexchange.com makes available various types of data on questions that have been asked on Stack Exchange’s multiple websites. This database was retrieved and among the pairs that it contained, those that had a high overlap of words were annotated with 1, and the rest 0. This approach was chosen because it is possible that two very differently framed questions have the same answer and hence, questions with similar phrasing are more likely to be paraphrases of each other.
2. _Synonym and Antonym replacement using MSRP database_ - Microsoft Research Paraphrase corpus consists of 5801 pairs of sentences, each accompanied by a binary judgment indicating whether human raters considered the pair of sentences to be similar enough in meaning to be considered close paraphrases. This project exported raw sentences from the MSRP dataset, performed preprocessing to remove null values. The stop words from the input sentences are pruned and tokenized. Parts of speech tagging (pos-tagging) is applied over the tokenized words. The algorithm identifies the adjectives and adverbs using the pos-tagging and these words are replaced by respective synonyms and antonyms using the Wordnet NLTK corpus.
3. _Passive-to-active conversion + Synonym/Antonym replacement or Word Substitution_ - Using sentences from the PAWS dataset, all the sentences are first converted from passive voice (if any) to active voice. For this, pass2act library has been used that utilizes SpaCy for parsing. Following that using in-built Python library “random”, it is chosen whether to replace any word from the sentence with its synonym, antonym, or any random word.
4. _Translation of sentences using google translate and synonym substitution_ - Using sentences from the STS-B dataset, we take an input sentence and perform a series of augmentations on it to retrieve varying levels of similar output sentences. There are two forms of augmentation used in this section: translation and substitution. For a high similarity, we would perform 1 translation and 1 substitution. For low similarity, we would perform 5 translations and 4 substitutions.
5. _Back Translation in PAWS_ - For the dataset generation in PAWS, Back Translation was used as mentioned in this paper. They translated English to German and then back to English to get paraphrases of the original language. This however can fail when the pair of sentences might be paraphrases but will be classified wrongly due to having major changes in the words in them. This is because German, or any most other western languages have Latin origin. Therefore, their sentence construction or similar etymological origin. 

## Group Members
 - Abhishek Jha
 - Matthew Jibben
 - Pauras Jadhav
 - Pooshpendu Adhikary
 - Rahul Sarikonda
 
## Mentored by
 - Dr Chitta Baral
 - Kuntal Pal

### Referenced Research Paper
[Semantic Textual SimilarityMultilingual and Cross-lingual Focused Evaluation](https://www.aclweb.org/anthology/S17-2001.pdf)
  - ### Other links
    - [MedSTS](https://arxiv.org/pdf/1808.09397.pdf)
    - [NLPProgess](https://nlpprogress.com/english/semantic_textual_similarity.html)
    - [SemEval](http://alt.qcri.org/semeval2017/task1/)
    - [STSBenckmark](http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark)
    - [PAWS](https://github.com/google-research-datasets/paws)

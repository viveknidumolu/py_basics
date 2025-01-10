# -*- coding: utf-8 -*-
"""DAY-7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16QMwlv45ZXYtVzj6ixYvcD_fWpRZhE8H

# Write a Python script that:
1. Use Genism to preprocess data from a sample text file, follow basic procedures like tokenization, stemming, lemmatization etc.
"""

#installing lib
!pip install gensim nltk

import gensim
from gensim.utils import simple_preprocess
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
# Tokenization
    tokens = simple_preprocess(text, deacc=True)
# Removing stopwords
    tokens = [word for word in tokens if word not in stop_words]
# Stemming
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
# Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]
    return lemmatized_tokens
with open("/content/sample.txt") as file:     #create a sample text file using notepad andcopy its path after uploading it in colab
    text = file.read()
processed_tokens = preprocess_text(text)
print("Original Text:")
print(text)
print("\nProcessed Tokens:")
print(processed_tokens)
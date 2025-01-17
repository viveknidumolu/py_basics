# -*- coding: utf-8 -*-
"""DAY-6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S8JqROdqGSqbZhLvnv2LKGLAnz2G6v7G

# Write a Python program to using NLTK and Spacy

*   Convert text to lowercase.
*   Remove stopwords using NLTK
"""

#installing libraries
!pip install nltk spacy

#using nltk and spacy to remove stop words and converting the processed text to lower case
import nltk
from nltk.corpus import stopwords
import spacy
nltk.download('stopwords')
def process_text(text):
    nlp = spacy.load("en_core_web_sm")     #converting upper to lower case
    doc = nlp(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [token.text for token in doc if token.text not in stop_words]
    return ' '.join(filtered_words)
input_text = "Natural Language Processing is a sub-field of Artificial Intelligence!"
result = process_text(input_text)
print("Original Text:")
print(input_text)
print("\nProcessed Text:")
print(result)
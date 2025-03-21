# -*- coding: utf-8 -*-
"""Day - 12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N8mMCOhmGCeRJgzANfSUVpNpSHr32QgI
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text, output_file):
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Save the word cloud image to a file
    plt.savefig(output_file, format='png')
    plt.close()

# Test the function with the given text
test_text = 'data science machine learning artificial intelligence'
output_image = 'wordcloud.png'
generate_wordcloud(test_text, output_image)
print(f"WordCloud saved as {output_image}")
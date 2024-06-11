'''
Write a Python program to count the frequency of words in a file.

'''
import re
from collections import defaultdict

def count_word_frequency(filename):
    word_freq = defaultdict(int)
    with open(filename, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                word_freq[word] += 1

    return dict(word_freq)

filename = 'example.txt' 
word_frequency = count_word_frequency(filename)
print("Word frequencies in the file:")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")

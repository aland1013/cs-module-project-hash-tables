import random
import re
from collections import defaultdict

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
delimiters = ['\n', ' ', ',', ':', '--', '\(', '\)', '\"']
word_list = re.split('|'.join(delimiters), words)
word_list = [w for w in word_list if w] # removes empty strings

d = defaultdict(list)

for i in range(len(word_list) - 1):
    word = word_list[i]
    next_word = word_list[i + 1]
    
    d[word].append(next_word)

start_words = [key for key in d.keys() if key[0].isupper()]
stop_words = [key for key in d.keys() if key[-1] in ['.', '!', '?']]

# TODO: construct 5 random sentences
# Your code here
def make_sentence(): 
    word = random.choice(start_words)
    print(word, end=" ")

    while word not in stop_words:
        word = random.choice(d[word])
        print(word, end=" ")

make_sentence()
make_sentence()
make_sentence()
make_sentence()
make_sentence()

# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from collections import defaultdict

with open("ciphertext.txt") as f:
    text = f.read()

char_list = list(text)

d = defaultdict(int)

for char in char_list:
    if char.isalpha():
        d[char] += 1

sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
cipher_keys = [k for k,v in sorted_d]

key = dict(zip(cipher_keys, ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']))

for char in char_list:
    if char in key:
        print(key[char], end='')
    else:
        print(char, end='')
        


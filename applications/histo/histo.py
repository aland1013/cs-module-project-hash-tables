# Your code here
from collections import defaultdict
with open("robin.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
word_list = words.split()
word_list = [word.strip(':;,.!?-+/\|[]{}()*^&"').lower() for word in word_list]

d = defaultdict(int)

for word in word_list:
    d[word] += 1

longest_word = max([len(k) for k in d.keys()])

data = [(k, v) for k, v in d.items()]
data.sort(key=lambda x: x[0])
data.sort(key=lambda x: x[1], reverse=True)
for d in data:
    spaces = ' '*(longest_word - len(d[0]) + 2)
    print(f"{d[0]}{spaces}{'#'*d[1]}")
from collections import defaultdict
import re

def word_count(s):
    # Your code here
    d = defaultdict(int)
    s = s.lower()
    arr = s.split()
    
    for word in arr:
        try:
            w = re.search('[\w\']+', word).group()
            d[w] += 1
            
        except:
            pass
    
    return d    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
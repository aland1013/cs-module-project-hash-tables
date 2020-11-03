from collections import defaultdict

def no_dups(s):
    # Your code here
    d = defaultdict(int)
    arr = s.split()
    
    for word in arr:
        d[word] += 1
    
    return ' '.join(d.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
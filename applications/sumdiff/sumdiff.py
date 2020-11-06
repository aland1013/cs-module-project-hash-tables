"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)

f(a) = f(c) - f(d) - f(b)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
import itertools

dict = {x: f(x) for x in q}

# generate a list of all pairs of numbers in q 
# in all possible orders and with repeated numbers
pairs = list(set(itertools.combinations_with_replacement(q, 2)) 
             | set(itertools.permutations(q, 2))) 

sums = {(a, b): dict[a] + dict[b] for a,b in pairs}
diffs = {(c, d): dict[c] - dict[d] for c,d in pairs}

# find all values that sums and diffs have in common
solution_set = (set(sums.values()) & set(diffs.values()))

for solution in solution_set:
    sum_pairs = [k for k,v in sums.items() if v == solution]
    diff_pairs = [k for k,v in diffs.items() if v == solution]
    
    for dp in diff_pairs:
        c = dp[0]
        d = dp[1]
        for sp in sum_pairs:
            a = sp[0]
            b = sp[1]
            print(f'f({a}) + f({b}) = f({c}) - f({d})    {dict[a]} + {dict[b]} = {dict[c]} - {dict[d]}')

    


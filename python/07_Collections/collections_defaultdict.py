'''
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
https://docs.python.org/3/library/collections.html#collections.defaultdict

defaultdict is a subclass of the built-in dict class. The main difference between defaultdict and dict is that when you try to access or modify a key that's not present in the dictionary, a default value is automatically given to that key.

d={}
d['Apple']=50
print(d['Grapes']) # This gives Key Error
print(d.get('Grapes',0)) # DEFAULTING
print(d) # {'Apple': 50}

d = defaultdict(int) ## inside parenthesis we say what should be the default value.
d['Apple']=50
print(d['Grapes']) ##→ no error, 'Grapes' will be added as a new key
print(d) # defaultdict(<class 'int'>, {'Apple': 50}

'''

from collections import defaultdict

n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

# using enumerate()

for b in B:
    if b in A:
        indices = [idx+1 for idx, val in enumerate(A) if val == b]
        print(*indices)
    else:
        print(-1)

# using enumerate() and defaultdict

d = defaultdict(list)

for idx, a in enumerate(A):
    d[a].append(idx+1)

for b in B:
    if b in d:
        print(*d[b])
    else:
        print(-1)

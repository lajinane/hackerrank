'''
https://www.hackerrank.com/challenges/compress-the-string/problem
https://docs.python.org/3/library/itertools.html#itertools.groupby

[k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
[list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

'''

from itertools import groupby

S = input()

for k, g in groupby(S):
    print((len(list(g)), int(k)), end=' ')

# OR

for k, g in groupby(S):
    print(f'({len(list(g))}, {k})', end=' ')

# OR

lst = [(len(list(g)), int(k)) for k, g in groupby(S)]
print(*lst)

'''
https://www.hackerrank.com/challenges/itertools-combinations/problem
https://docs.python.org/3/library/itertools.html#itertools.combinations

combinations('ABCD', 2) --> AB AC AD BC BD CD

'''

from itertools import combinations

S, K = input().split()
S = sorted(S)
K = int(K)

for k in range(1, K+1):
    tuples = list(combinations(S, k))
    lst = ["".join(_) for _ in tuples]
    print(*lst, sep='\n')

# OR

for k in range(1, K+1):
    tuples = list(combinations(S, k))
    for _ in tuples:
        print("".join(_))

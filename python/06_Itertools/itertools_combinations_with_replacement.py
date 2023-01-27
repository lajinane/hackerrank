'''
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement

combinations('ABC', 2) --> AB, AC, BC
combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC

'''

from itertools import combinations_with_replacement

S, K = input().split()
S = sorted(S)
K = int(K)

tuples = list(combinations_with_replacement(S, K))
lst = ["".join(_) for _ in tuples]
print(*lst, sep='\n')

# OR

tuples = list(combinations_with_replacement(S, K))
for _ in tuples:
    print("".join(_))

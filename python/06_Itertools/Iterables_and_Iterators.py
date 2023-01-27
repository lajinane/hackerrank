'''
https://www.hackerrank.com/challenges/iterables-and-iterators/problem
https://docs.python.org/3/library/itertools.html

combinations('ABCD', 2) --> AB AC AD BC BD CD

'''

from itertools import combinations

N = int(input())
S = input().split()
K = int(input())

combs = list(combinations(S, K))

# using list comprehension

a_occ = [_ for _ in combs if 'a' in _]
print(round(len(a_occ)/len(combs), 3))

# using filter and lambda

a_occ = list(filter(lambda _: 'a' in _, combs))
print(f'{len(a_occ)/len(combs):.3f}')

# OR simply

num = 0
for c in combs:
    num += 'a' in c
print(float(num)/len(combs))

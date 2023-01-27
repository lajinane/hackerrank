'''
https://www.hackerrank.com/challenges/maximize-it/problem
'''

from itertools import product

K, M = map(int, input().split())
lst = [list(map(int, input().split()))[1:] for _ in range(K)]

prods = [*list(product(*lst))]
prods_sums = [sum([_**2 for _ in p]) % M for p in prods]
print(max(prods_sums))

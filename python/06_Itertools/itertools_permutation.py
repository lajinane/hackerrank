'''
https://www.hackerrank.com/challenges/itertools-permutations/problem
https://docs.python.org/3/library/itertools.html#itertools.permutations

permutations('ABC', 2) --> AB AC BA BC CA CB
permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC

'''

from itertools import permutations

S, K = input().split()
K = int(K)


for i in permutations(sorted(S), K):
    print("".join(i))

# OR

for i in permutations(sorted(S), K):
    print(*i, sep="")

# OR

lst = ["".join(_) for _ in sorted(permutations(S, K))]
print(*lst, sep="\n")

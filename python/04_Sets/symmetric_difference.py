'''
https://www.hackerrank.com/challenges/symmetric-difference/problem
'''

# method 1

N = int(input())
sN = set(list(map(int, input().split())))
M = int(input())
sM = set(list(map(int, input().split())))

symmetric = list(sN.difference(sM).union(sM.difference(sN)))
print(*sorted(symmetric), sep="\n")

# method 2

N, sN = int(input()), set(map(int, input().split()))
M, sM = int(input()), set(map(int, input().split()))

symmetric = list(sN.difference(sM)) + list(sM.difference(sN))
print(*sorted(symmetric), sep="\n")

# method 3

N, sN = int(input()), {int(i) for i in input().split()}
M, sM = int(input()), {int(i) for i in input().split()}

symmetric = list(sN.symmetric_difference(sM))
print(*sorted(symmetric), sep="\n")

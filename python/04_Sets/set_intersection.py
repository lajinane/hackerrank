'''
https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
'''

N, sN = int(input()), set(input().split())
B, sB = int(input()), set(input().split())

# method 1 - using & operator
print(len(sN & sB))

# method 2 - using intersection()
print(len(sN.intersection(sB)))

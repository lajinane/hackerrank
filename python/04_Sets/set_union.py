'''
https://www.hackerrank.com/challenges/py-set-union/problem
'''

N, sN = int(input()), set(input().split())
B, sB = int(input()), set(input().split())

# method 1 - using | operator
print(len(sN | sB))

# method 2 - using union()
print(len(sN.union(sB)))

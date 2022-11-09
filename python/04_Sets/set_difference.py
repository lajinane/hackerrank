'''
https://www.hackerrank.com/challenges/py-set-difference-operation/problem
'''

N, sN = int(input()), set(input().split())
B, sB = int(input()), set(input().split())

# method 1 - using - operator
print(len(sN - sB))

# method 2 - using difference()
print(len(sN.difference(sB)))

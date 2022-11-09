'''
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
'''

N, sN = int(input()), set(input().split())
B, sB = int(input()), set(input().split())

# method 1 - using ^ operator
print(len(sN ^ sB))

# method 2 - using symmetric_difference()
print(len(sN.symmetric_difference(sB)))

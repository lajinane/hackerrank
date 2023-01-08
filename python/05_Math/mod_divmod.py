'''
https://www.hackerrank.com/challenges/python-mod-divmod/problem
'''

a, b = int(input()), int(input())

print(a // b)  # quotient of integer division
print(a % b)   # remainder of integer division
print(divmod(a, b))

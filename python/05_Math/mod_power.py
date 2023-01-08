'''
https://www.hackerrank.com/challenges/python-power-mod-power/problem

>>> 2**3 
8
>>> pow(2,3) # 2*2*2
8
>>> pow(2,-3) # 1 / (2**-3)
0.125
>>> pow(2,3,4) # (2**3) % 4
0
>>> pow(2,3,3) # (2**3) % 3
2

pow(a,b) : b can be negative
pow(a,b,m) : b cannot be negative

'''

a, b, m = int(input()), int(input()), int(input())

print(pow(a, b))
print(pow(a, b, m))

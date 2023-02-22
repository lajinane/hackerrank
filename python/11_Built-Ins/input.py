'''
https://www.hackerrank.com/challenges/input/problem

>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
'''

x, k = map(int, input().split())
Px = input()
print(eval(Px) == k)

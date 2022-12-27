'''
https://www.hackerrank.com/challenges/py-check-subset/problem

http://stackoverflow.com/questions/27674289/the-complextiy-of-python-issubset

https://codedestine.com/python-set-subset-example/

issubset :
can work with any iterable.
< Set Object >.issubset( <iterable object> )

Operator <= :
can work only with set objects
< Set Object 1 > <= < Set Object 2 > : To check subset relationship
< Set Object 1 > < < Set Object 2 > : To check strict subset relationship
'''

T = int(input())
for _ in range(T):
    nA, sA = int(input()), set(map(int, input().split()))
    nB, sB = int(input()), set(map(int, input().split()))

    # method 1 - issubset()
    print(sA.issubset(sB))

    # method 2 - operator <=
    print(sA <= sB)

    # method 3 - intersection
    print(sA & sB == sA)

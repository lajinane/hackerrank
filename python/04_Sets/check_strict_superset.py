'''
https://www.hackerrank.com/challenges/py-check-strict-superset/problem

https://codedestine.com/python-set-subset-example/
https://codedestine.com/python-set-superset-example/

issuperset : 
can work with any iterable.
< Set Object >.issuperset( <iterable object> ) 

issubset :
can work with any iterable.
< Set Object >.issubset( <iterable object> )

Operator <= :
can work only with set objects
< Set Object 1 > <= < Set Object 2 > : To check subset relationship
< Set Object 1 > < < Set Object 2 > : To check strict subset relationship

        # if not S < A:
        # if not S.issubset(A) OR len(S) >= len(A)
'''


A = set(map(int, input().split()))
N = int(input())

# method 1 - issuperset()
isAsuperset = True
for _ in range(N):
    S = set(map(int, input().split()))
    if not A.issuperset(S):
        isAsuperset = False
        break
print(isAsuperset)

# method 2 - list , all() , issuperset()
sets = [set(map(int, input().split())) for _ in range(N)]
print(all([A.issuperset(s) for s in sets]))

# method 2 - list , all() , operator <
sets = [set(map(int, input().split())) for _ in range(N)]
print(all([s < A for s in sets]))

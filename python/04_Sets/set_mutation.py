'''
https://www.hackerrank.com/challenges/py-set-mutations/problem
'''

A, sA = int(input()), set(input().split())
N = int(input())

for _ in range(N):
    ((cmd, B), sB) = (input().split(), set(input().split()))
    eval(f'sA.{cmd}({sB})')

print(sum(list(map(int, sA))))

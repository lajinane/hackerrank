'''
https://www.hackerrank.com/challenges/py-set-add/problem
'''

# method - loop and add()

N = int(input())
s = set()
for _ in range(N):
    s.add(input())
print(len(s))

# method - set comprehension

N = int(input())
s = {input() for _ in range(N)}
print(len(s))

# method - set comprehension

s = set(input() for _ in range(int(input())))
print(len(s))

# method - list comprehension

N = int(input())
s = set([input() for _ in range(N)])
print(len(s))

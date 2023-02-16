'''
https://www.hackerrank.com/challenges/py-collections-deque/problem
https://docs.python.org/3/library/collections.html#collections.deque
https://www.geeksforgeeks.org/python-getattr-method/

Queue -> First-In First-Out (FIFO)
A deque is a double-ended queue. It can be used to add or remove elements from both ends  with approximately O(1).

>>> d = deque('abc')
deque(['a', 'b', 'c'])
>>> d.append('d')
deque(['a', 'b', 'c', 'd'])
>>> d.popleft()
'a'

>>> d = deque('cba')
>>> d.appendleft('d')
deque(['d', 'c', 'b', 'a'])
>>> d.pop()
'a'

getattr(object, attribute[, default])(args)
The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.

'''

from collections import deque

n = int(input())

# using classic methods

d = deque()

for _ in range(n):
    cmd, *args = input().lower().strip().split()
    # args = [int(i) for i in args]

    if cmd == 'append':
        d.append(args[0])
    elif cmd == 'appendleft':
        d.appendleft(args[0])
    elif d and cmd == 'pop':
        d.pop()
    elif d and cmd == 'popleft':
        d.popleft()

print(*d)

# OR using getattr

d = deque()

for _ in range(n):
    cmd, *args = input().lower().strip().split()
    getattr(d, cmd)(*args)

print(*d)

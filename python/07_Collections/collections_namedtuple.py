'''
https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
https://docs.python.org/3/library/collections.html#collections.namedtuple

>>> Point = namedtuple('Point','x,y')
<class '__main__.Point'>
>>> pt1 = Point(1,2)
Point(x=1, y=2)
>>> pt1.x
1

'''

from collections import namedtuple

n = int(input())
columns = input().strip()

Student = namedtuple('Student', columns)

rows = [Student(*input().strip().split()) for _ in range(n)]

average = sum([int(_.MARKS) for _ in rows]) / n
print(f"{average:.2f}")

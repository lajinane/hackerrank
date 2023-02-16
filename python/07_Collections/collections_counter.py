'''
https://www.hackerrank.com/challenges/collections-counter/problem
https://docs.python.org/3/library/collections.html#collections.Counter

>>> Counter('gallahad')
Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
>>> Counter(['eggs', 'ham'])
Counter({'eggs': 1, 'ham': 1})
>>> Counter(cats=4, dogs=8)
Counter({'dogs': 8, 'cats': 4})

'''

from collections import Counter

x = int(input())
sizes = list(map(int, input().split()))
n = int(input())
customers = [list(map(int, input().split())) for _ in range(n)]

sizes_counter = Counter(sizes)

total = 0
for i in customers:
    size, price = i[0], i[1]
    if size in sizes_counter and sizes_counter[size] > 0:
        sizes_counter[size] -= 1
        total += price

print(total)

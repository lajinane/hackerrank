'''
https://www.hackerrank.com/challenges/no-idea/problem
'''

from collections import Counter

N, M = map(int, input().split())
lst = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

# method 1
for i in lst:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

# method 2
happiness = sum(1 if i in A else -1 if i in B else 0 for i in lst)

# method 3 - play with booleans
happiness = sum((i in A) - (i in B) for i in lst)

# method 4 - Counter()
count = Counter(lst)
happiness = sum(count.get(i, 0) for i in A) - sum(count.get(i, 0) for i in B)

# method 6
likes = [1 for i in lst if i in A]
dislikes = [-1 for i in lst if i in B]
happiness = sum(likes + dislikes)
# OR
# happiness = len(likes) - len(dislikes)

print(happiness)

'''
https://www.hackerrank.com/challenges/zipped/problem

>>> print(*zip([1,2,3,4,5,6],'Hack'))
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k')]

'''

n, x = map(int, input().split())

marks = [list(map(float, input().split())) for _ in range(x)]

marks_by_subject = zip(*marks)

[print(sum(item)/len(item)) for item in marks_by_subject]

'''
https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
'''

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

# using sorted() and lambda
arr = sorted(arr, key=lambda item: item[k])

# using sort() and lambda
arr.sort(key=lambda item: item[k])

[print(*_) for _ in arr]

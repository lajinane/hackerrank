'''
https://www.hackerrank.com/challenges/triangle-quest-2/problem
'''


for i in range(1, int(input())+1):
    print((10 ** i // 9) ** 2)

# OR

for i in range(1, int(input())+1):
    print(*list(range(1, i+1)), *list(range(i-1, 0, -1)), sep='')

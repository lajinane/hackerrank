'''
https://www.hackerrank.com/challenges/piling-up/problem
'''

for _ in range(int(input())):

    size = int(input())
    blocks = list(map(int, input().split()))

    # check for an element in the middle that is greater than both its neighbors

    for i in range(1, size - 1):
        if blocks[i] > blocks[i-1] and blocks[i] > blocks[i+1]:
            print('No')
            break
    else:
        print('Yes')

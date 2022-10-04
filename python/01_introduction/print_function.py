'''
https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
'''

if __name__ == '__main__':
    n = int(input())

    # method 1
    print(*range(1, n+1), sep='', end='\n')

    # method 2
    print(''.join(map(str, range(1, n+1))))

    # method 3
    for _ in range(n):
        print(_ + 1, end='')

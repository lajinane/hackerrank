'''
https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    # method 1
    print(a//b)
    print(a/b)

    # method 2
    print(a//b, a/b, sep='\n')

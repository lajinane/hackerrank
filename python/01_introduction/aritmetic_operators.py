'''
https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    # method 1
    print(a+b)
    print(a-b)
    print(a*b)

    # method 2
    print(a+b, a-b, a*b, sep='\n')

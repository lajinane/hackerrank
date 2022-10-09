'''
https://www.hackerrank.com/challenges/python-tuples/problem
'''

if __name__ == '__main__':
    n = int(input())

    # method 1
    tup = tuple(list(map(int, input().strip().split()))[:n])
    print(hash(tup))

    # method 2
    tup = tuple([int(i) for i in input().strip().split()][:n])
    print(hash(tup))

    # method 3
    tup = tuple(map(int, input().split()))
    print(hash(tup))

    # method 4
    tup = tuple(int(i) for i in input().split())
    print(hash(tup))

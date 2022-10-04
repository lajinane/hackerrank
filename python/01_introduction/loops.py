'''
https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
'''

if __name__ == '__main__':
    n = int(input())

    # method 1
    for i in range(n):
        print(i ** 2)

    # method 2
    for i in range(n):
        print(i * i)

    # method 3 - using list comprehension - with loop
    for _ in [x ** 2 for x in range(n)]:
        print(_)

    # method 4 - using list comprehension - without loop
    print(*[x ** 2 for x in range(n)], sep='\n')

    # method 4 - using map
    print('\n'.join(map(str, [x ** 2 for x in range(n)])))

    # method 5 - using list comprehension
    # an expression is assigned to nothing
    [print(i ** 2) for i in range(n)]

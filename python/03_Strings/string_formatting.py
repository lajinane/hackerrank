'''
https://www.hackerrank.com/challenges/python-string-formatting/problem
'''


from turtle import width


def print_formatted(number):
    ''' f-string and rjust() '''
    width = len(f'{number:b}')
    for i in range(1, number+1):
        print(f'{i:d}'.rjust(width),
              f'{i:o}'.rjust(width),
              f'{i:X}'.rjust(width),
              f'{i:b}'.rjust(width))


def print_formatted_2(number):
    ''' f-string and width '''
    width = len(f'{number:b}')
    for i in range(1, number+1):
        print(f'{i:>{width}d}',
              f'{i:>{width}o}',
              f'{i:>{width}X}',
              f'{i:>{width}b}')


def print_formatted_3(number):
    ''' str.format() and width '''
    width = len(f'{number:b}')
    for i in range(1, number+1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(
            i, width=width))


def print_formatted_4(number):
    ''' str.format() and width '''
    width = len(f'{number:b}')
    text = '{0:>{1}d} {0:>{1}o} {0:>{1}X} {0:>{1}b}'
    for i in range(number):
        print(text.format(i+1, width))


def print_formatted_5(number):
    ''' oct(), hex(), bin() and rjust() '''
    width = len(bin(number)) - 2
    for i in range(1, number+1):
        print(str(i).rjust(width),
              oct(i)[2:].rjust(width),
              hex(i)[2:].upper().rjust(width),
              bin(i)[2:].rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

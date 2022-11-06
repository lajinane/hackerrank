'''
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''

import string
alphabet = list(string.ascii_lowercase)


def print_rangoli(size):
    ''' using one loop, string concatenation, and list reverse '''
    letters = alphabet[:size]
    width = size*4-3
    lines = []
    for i in range(size):

        # method 1
        s = '-'.join(letters[:i:-1] + letters[i:])

        # method 2
        s = '-'.join(letters[size-1:i:-1] + letters[i:])

        # method 3
        s = '-'.join(c for c in letters[i:])
        s = s[::-1][:-1] + s

        # method 4
        s = letters[i]
        for c in letters[i+1:]:
            s = f'{c}-{s}-{c}'

        lines.append(s.center(width, '-'))

    lines = lines[::-1][:-1] + lines
    print(*lines, sep='\n')


def print_rangoli_2(size):
    ''' using two loops and join '''
    letters = list(map(chr, range(ord('a'), ord('z')+1)))[:size]
    width = size*4-3
    for i in range(size-1, 0, -1):
        print('-'.join(letters[:i:-1]+letters[i:]).center(width, '-'))
    for i in range(size):
        print('-'.join(letters[:i:-1]+letters[i:]).center(width, '-'))


def print_rangoli_3(size):
    ''' using four loops '''
    letters = list(map(chr, range(97, 123)))[:size]
    width = size*4-3
    for i in range(size):
        s = letters[size - i - 1]
        for j in range(size - i, size):
            s = f'{letters[j]}-{s}-{letters[j]}'
        print(s.center(width, '-'))
    for i in range(1, size):
        s = letters[i]
        for j in range(i+1, size):
            s = f'{letters[j]}-{s}-{letters[j]}'
        print(s.center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

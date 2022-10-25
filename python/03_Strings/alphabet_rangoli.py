'''
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''


def print_rangoli(size):
    letters = list(map(chr, range(97, 123)))[:size]
    width = size * 3
    for i in range(size - 1, 0, -1):
        ri = size - 1 - i
        print(i, ri, letters[i].center(width, '-'))
    print(letters[0].center(width, '-'))
    for i in range(1, size):
        ri = size - 1 - i
        print(i, ri, letters[i].center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

'''
https://www.hackerrank.com/challenges/swap-case/problem
'''


def swap_case(s):
    return s.swapcase()


def swap_case_2(s):
    swap = ''
    for i in s:
        swap += (i.upper() if i.islower() else i.lower())
    return swap


def swap_case_3(s):
    lst = [(i.upper() if i.islower() else i.lower()) for i in s]
    return ''.join(lst)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

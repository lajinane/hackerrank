''''
https://www.hackerrank.com/challenges/nested-list/problem
'''

# old formatting : % and str.format
# new formatting : formatted string literal or f-string
# Using round(avg, 2) is not suitable, 56 rounded to 56.0 instead of 56.00

from functools import reduce
from statistics import mean


def average(lst):
    ''' Using sum() '''
    return float(sum(lst)/len(lst))


def average_2(lst):
    ''' Using reduce() and lambda '''
    return reduce(lambda a, b: a + b, lst) / len(lst)


def average_3(lst):
    ''' Using mean '''
    return mean(lst)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    lst = student_marks[query_name]
    avg = average(lst)

    # method 1 - Using %
    print('%.2f' % avg)

    # method 2 - Using str.format()
    print('{0:.2f}'.format(avg))

    # method 3 - Using f-string
    print(f'{avg:.2f}')

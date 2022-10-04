'''
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
'''


def is_leap_1(year):
    ''' method 1 '''
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def is_leap_2(year):
    ''' method 2 '''
    return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))


def is_leap(year):
    ''' method 3 '''
    return year % 400 == 0 or (not year % 100 == 0 and year % 4 == 0)


year = int(input())
print(is_leap(year))

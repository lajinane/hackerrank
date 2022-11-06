'''
https://www.hackerrank.com/challenges/capitalize/problem
'''

import math
import os
import random
import re
import sys


def solve(s):
    ''' using using split, join and capitalize '''
    return ' '.join(w.capitalize() for w in s.split(' '))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

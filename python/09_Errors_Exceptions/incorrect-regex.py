'''
https://www.hackerrank.com/challenges/incorrect-regex/problem
https://docs.python.org/3/tutorial/errors.html
https://docs.python.org/3/library/re.html
'''

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)

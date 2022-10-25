'''
https://www.hackerrank.com/challenges/string-validators/problem
'''

import re

if __name__ == '__main__':
    s = input()

    # method 1 - string methods
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

    # method 2 - string methods
    print(any([c.isalnum() for c in s]))
    print(any([c.isalpha() for c in s]))
    print(any([c.isdigit() for c in s]))
    print(any([c.islower() for c in s]))
    print(any([c.isupper() for c in s]))

    # method 3 - eval
    for fct in ['alnum', 'alpha', 'digit', 'lower', 'upper']:
        print(any([eval(f'char.is{fct}()') for char in s]))

    # method 3 - regex
    print(bool(re.search(r'[a-z,A-Z,0-9]', s)))
    print(bool(re.search(r'[a-z,A-Z]', s)))
    print(bool(re.search(r'[0-9]', s)))
    print(bool(re.search(r'[a-z]', s)))
    print(bool(re.search(r'[A-Z]', s)))

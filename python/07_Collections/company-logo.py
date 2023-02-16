'''
https://www.hackerrank.com/challenges/most-commons/problem
https://docs.python.org/3/library/collections.html#collections.Counter
'''

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = sorted(input())

    c = Counter(s).most_common(3)

    for i, v in c:
        print(i, v)

    # [print(*_) for _ in c]

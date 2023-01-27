'''
https://www.hackerrank.com/challenges/itertools-product/problem
https://docs.python.org/3/library/itertools.html#itertools.product

product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
'''

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*list(product(A, B)))

# OR

for item in product(A, B):
    print(item, end=' ')

# OR

C = [A, B]
print(*list(product(*C)))

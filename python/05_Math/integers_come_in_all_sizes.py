'''
https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem

c++ int limit 2^31 - 1
c++ long long int limit 2^63 - 1
python int has no limit

'''

a, b, c, d = int(input()), int(input()), int(input()), int(input())

print(a**b + c**d)
# OR
print(pow(a, b)+pow(c, d))

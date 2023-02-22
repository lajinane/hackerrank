'''
https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
https://www.geeksforgeeks.org/any-all-in-python/
https://www.geeksforgeeks.org/python-program-to-check-if-number-is-palindrome-one-liner/

palindromic number:
12321 => True
1234  => False

'''

n = int(input())
arr = list(map(int, input().split()))

positive = [i > 0 for i in arr]
palindromic = [str(i) == str(i)[::-1] for i in arr]

print(all(positive) and any(palindromic))

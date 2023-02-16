'''
https://www.hackerrank.com/challenges/word-order/problem
'''

from collections import Counter

n = int(input())
words = [input() for _ in range(n)]

words_count = Counter(words)

print(len(words_count))
print(*words_count.values())

'''
https://www.hackerrank.com/challenges/designer-door-mat/problem
'''

n, m = map(int, input().split())
pattern = '.|.'
welcome = 'WELCOME'

# method 1
for i in range(1, n+1):
    ri = n-i+1
    width = n-abs(i-ri)
    line_pattern = welcome if i == ri else pattern * width
    print(line_pattern.center(m, '-'))

# method 2
for i in range(1, n, 2):
    print((pattern * i).center(m, '-'))
print(welcome.center(m, '-'))
for i in range(n-2, -1, -2):
    print((pattern * i).center(m, '-'))

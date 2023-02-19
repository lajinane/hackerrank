'''
https://www.hackerrank.com/challenges/exceptions/problem
https://docs.python.org/3/tutorial/errors.html
'''

for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)

    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

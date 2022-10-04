'''
https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
'''

if __name__ == '__main__':
    n = int(input().strip())
    print("Weird" if n % 2 != 0 or n in range(6, 20) else "Not Weird")

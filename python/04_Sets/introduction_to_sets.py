'''
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
'''


def average(array):
    s_array = set(array)
    return round(sum(s_array) / len(s_array), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

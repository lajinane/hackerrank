'''
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''

# arr = <map object at ...>
# list(arr) = [2, 3, 5, 6, 6]
# set(arr) = {2, 3, 5, 6}
# list(set(arr)) = [2, 3, 5, 6]
# Counter(arr) = Counter({6: 2, 2: 1, 3: 1, 5: 1})
# list(Counter(arr)) = [2, 3, 6, 5]
# Counter(arr).keys() = dict_keys([2, 3, 6, 5])
# list(Counter(arr).keys()) = [2, 3, 6, 5]


from collections import Counter

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # method 1
    print(sorted(list(set(arr)))[-2])

    # method 2
    print(sorted(list(set(arr)), reverse=True)[1])

    # method 3
    unq_arr = list(set(arr))
    unq_arr.sort()
    print(unq_arr[-2])

    # method 4
    unq_arr = list(set(arr))
    unq_arr.sort(reverse=True)
    print(unq_arr[1])

    # method 5
    print(sorted(list(Counter(arr)))[-2])

    # method 6
    print(sorted(list(Counter(arr).keys()))[-2])

    # method 7
    unq_arr = list(Counter(arr))
    unq_arr.sort()
    print(unq_arr[-2])

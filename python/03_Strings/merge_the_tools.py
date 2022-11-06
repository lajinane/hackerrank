'''
https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

# set() won't work, returns distinct items, but without order

from collections import OrderedDict


def merge_the_tools(string, k):
    ''' using dict.fromkeys()'''
    n = len(string)
    for i in range(0, n, k):
        t = string[i: i+k]
        u = "".join(dict.fromkeys(t))
        print(u)


def merge_the_tools_2(string, k):
    ''' using OrderedDict.fromkeys() '''
    n = len(string)
    for i in range(0, n, k):
        t = string[i: i+k]
        u = "".join(OrderedDict.fromkeys(t))
        print(u)


def merge_the_tools_3(string, k):
    ''' hashing using a dictionary '''
    n = len(string)
    for i in range(0, n, k):
        t = string[i:i+k]
        u = "".join({key: 0 for key in t})
        print(u)


def merge_the_tools_4(string, k):
    ''' using a loop '''
    num_t = int(len(string)/k)
    for i in range(num_t):
        t = string[i*k: (i+1)*k]
        u = ""
        for c in t:
            if c not in u:
                u += c
        print(u)


def merge_the_tools_5(string, k):
    ''' using list comprehension '''
    num_t = int(len(string)/k)
    for i in range(num_t):
        t = string[i*k: (i+1)*k]
        u = ""
        print("".join([u for c in t if c not in u]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

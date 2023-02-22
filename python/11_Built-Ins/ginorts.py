'''
https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

>>> ord('a')
97
>>> chr(97)
'a'
>>> ''.join(sorted('Hello World!'))
' !HWdellloor'
>>> ''.join(sorted('Hello World!',key=lambda x:x.lower()))
' !deHllloorW'

Ascii:
a-z   97-122
A-Z   65-90
0-9   48–57

'''


# using sorted(), join() and list comprehension

def sorting_1(s):
    ''' using sorted() and list comprehension '''
    lower = sorted([_ for _ in s if _.islower()])
    upper = sorted([_ for _ in s if _.isupper()])
    odd = sorted([_ for _ in s if _.isnumeric() and int(_) % 2 == 1])
    even = sorted([_ for _ in s if _.isnumeric() and int(_) % 2 == 0])
    return ''.join(lower + upper + odd + even)


def sorting_2(s):
    ''' using sorted() and filter(lambda) '''
    lower = sorted(filter(lambda x: x.islower(), s))
    upper = sorted(filter(lambda x: x.isupper(), s))
    odd = sorted(filter(lambda x: x.isdigit() and int(x) % 2 == 1, s))
    even = sorted(filter(lambda x: x.isdigit() and int(x) % 2 == 0, s))
    return ''.join(lower + upper + odd + even)


def sorting_3(s):
    ''' using loop and lists '''
    lower, upper, odd, even = [], [], [], []
    for c in s:
        if c.isalpha():
            if c.islower():
                lower.append(c)
            elif c.isupper():
                upper.append(c)
        else:
            if int(c) % 2 == 0:
                even.append(c)
            else:
                odd.append(c)
    return ''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even))


def sorting_func(c):
    if c.isalpha():
        return ord(c) if c.islower() else ord(c)+100
    elif c.isdigit():
        return ord(c)+200 if int(c) % 2 == 1 else ord(c)+300
    return 0


def sorting(s):
    return ''.join(sorted(s, key=sorting_func))


s = 'Sorting1234'
print(sorting(s))  # ginortS1324

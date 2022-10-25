'''
https://www.hackerrank.com/challenges/text-wrap/problem

https://docs.python.org/3/library/textwrap.html
'''

# textwrap.wrap(text, width)
# # returns a list of strings, length of each item <= width

# textwrap.fill(text, width)
# # returns a string with newlines i.e. paragraph, length of each line <= width


import textwrap


def wrap(string, max_width):
    ''' fill '''
    return textwrap.fill(string, max_width)


def wrap_2(string, max_width):
    ''' wrap and join'''
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

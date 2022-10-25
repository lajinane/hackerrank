'''
https://www.hackerrank.com/challenges/find-a-string/problem
'''

import re


def count_substring(string, sub_string):
    ''' while and find '''
    cnt = 0
    ocr = string.find(sub_string)
    while ocr != -1:
        cnt += 1
        ocr = string.find(sub_string, ocr+1)
    return cnt


def count_substring_2(string, sub_string):
    ''' regex '''
    return len(re.findall(f'(?={sub_string})', string))


def count_substring_3(string, sub_string):
    ''' for and match '''
    cnt = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            cnt += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

'''
https://www.hackerrank.com/challenges/whats-your-name/problem
'''

#
# old formatting : % and str.format
# new formatting : formatted string literal or f-string
#


def print_full_name(first, last):
    ''' f-string '''
    print(f'Hello {first} {last}! You just delved into python.')


def print_full_name_2(first, last):
    ''' + string concatenation '''
    print('Hello ' + first + ' ' + last + '! You just delved into python.')


def print_full_name_3(first, last):
    ''' str.format() '''
    print('Hello {} {}! You just delved into python.'.format(first, last))


def print_full_name_4(first, last):
    ''' % operator '''
    print('Hello %s %s! You just delved into python.' % (first, last))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

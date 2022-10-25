'''
https://www.hackerrank.com/challenges/python-mutations/problem
'''


def mutate_string(string, position, character):
    ''' slice and join => better performance '''
    return string[:position] + character + string[position+1:]


def mutate_string_2(string, position, character):
    ''' list and set '''
    lst = list(string)
    lst[position] = character
    return ''.join(lst)


def mutate_string_3(string, position, character):
    ''' list and pop '''
    lst = list(string)
    lst.pop(position)
    lst.insert(position, character)
    return ''.join(lst)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

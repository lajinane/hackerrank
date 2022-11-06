'''
https://www.hackerrank.com/challenges/the-minion-game/problem
'''


def minion_game(string):
    string = string.upper()
    vowels = 'AEIOU'
    n = len(string)

    score_c = score_v = 0
    for i in range(n):
        if string[i] in vowels:
            score_v += n - i
        else:
            score_c += n - i

    if score_c > score_v:
        print(f'Stuart {score_c}')
    elif score_c < score_v:
        print(f'Kevin {score_v}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

'''
https://www.hackerrank.com/challenges/list-comprehensions/problem
'''

if __name__ == '__main__':

    # x, y, z, n = [int(input()) for _ in range(4)]
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # method 1
    pairs = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i + j + k != n:
                    pairs.append([i, j, k])

    # method 2
    pairs = [[i, j, k] for i in range(x+1) for j in range(y+1)
             for k in range(z+1) if i+j+k != n]

    # method 3
    all_pairs = [[i, j, k]
                 for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    pairs = list(filter(lambda sub_list: sum(sub_list) != n, all_pairs))

    print(pairs)

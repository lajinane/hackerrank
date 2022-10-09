'''
https://www.hackerrank.com/challenges/nested-list/problem
'''

if __name__ == '__main__':

    # method 1
    tuples = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        tuples.append((name, score))

    scores = [x[1] for x in tuples]
    second_lowest_score = sorted(set(scores))[1]
    second_lowest_tuples = [
        tup for tup in tuples if tup[1] == second_lowest_score]
    second_lowest_names = sorted([x[0] for x in second_lowest_tuples])
    print(*second_lowest_names, sep='\n')

    # method 2
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = [x[1] for x in students]
    scores_no_duplicated = list(set(scores))
    second_lowest = sorted(scores_no_duplicated)[1]

    second_lowest_scores = [x for x in students if second_lowest in x]
    second_lowest_names = [x[0] for x in second_lowest_scores]

    for name in sorted(second_lowest_names):
        print(name)

    # method 3
    students = [[input(), float(input())] for x in range(int(input()))]
    scores = sorted(set([x[1] for x in students]))
    for name in sorted(x[0] for x in students if x[1] == scores[1]):
        print(name)

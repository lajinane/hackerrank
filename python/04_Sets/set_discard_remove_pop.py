'''
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
'''

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, *args = input().strip().split()

    # method 1
    args = [int(_) for _ in args]
    if cmd == 'pop':
        s.pop()
    elif cmd == 'discard':
        s.discard(args[0])
    elif cmd == 'remove':
        s.remove(args[0])

    # method 2
    if cmd == 'pop':
        s.pop()
    else:
        eval(f's.{cmd}({args[0]})')

print(sum(s))

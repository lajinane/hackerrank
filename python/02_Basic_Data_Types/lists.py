'''
https://www.hackerrank.com/challenges/python-lists/problem
'''

if __name__ == '__main__':
    n = int(input())
    lst = []

    for i in range(n):
        cmd, *args = input().strip().split()

        # method 1
        args = [int(i) for i in args]
        if cmd == 'print':
            print(lst)
        elif cmd == 'insert':
            lst.insert(args[0], args[1])
        elif cmd == 'remove':
            lst.remove(args[0])
        elif cmd == 'append':
            lst.append(args[0])
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()

        # method 2
        if cmd == 'print':
            print(lst)
        else:
            eval(f'lst.{cmd}({",".join(filter(None, args))})')

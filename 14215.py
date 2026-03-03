import sys

a, b, c = map(int, sys.stdin.readline().split())

lst = [a, b, c]
max_line = max(a, b, c)
lst.remove(max_line)
if max_line >= sum(lst):
    for i in range(max_line, 0, -1):
        if i < sum(lst):
            print(i + sum(lst))
            break
else:
    print(a + b + c)

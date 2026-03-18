import sys

N = int(sys.stdin.readline())


if N == 1:
    a = int(sys.stdin.readline())
    print(a**2)
else:
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    print(lst[0]*lst[-1])

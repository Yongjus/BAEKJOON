import sys

N = int(sys.stdin.readline())

set_N = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if lst[i] in set_N:
        print(1, end=" ")
    else:
        print(0, end=" ")

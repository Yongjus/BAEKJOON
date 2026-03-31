import sys

N = int(sys.stdin.readline())
set_N = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
lst_M = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    print(int(lst_M[i] in set_N))

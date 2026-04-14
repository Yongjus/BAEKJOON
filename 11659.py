import sys

N, M = map(int, sys.stdin.readline().split())
N_lst = list(map(int, sys.stdin.readline().split()))

cumsum = [0]*(N+1)

for i in range(1, N+1):
    cumsum[i] = cumsum[i-1] + N_lst[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(cumsum[j] - cumsum[i-1])

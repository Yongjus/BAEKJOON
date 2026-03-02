import sys

N, M = map(int, sys.stdin.readline().split())

A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

B = []
for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))


for i in range(N):
    res = []
    for j in range(M):
        res.append(A[i][j] + B[i][j])
    print(*res)

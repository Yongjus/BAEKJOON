import sys

N, K = map(int, sys.stdin.readline().split())

C = 1
for k in range(K):
    C *= N-k
    C /= k+1
print(int(C))

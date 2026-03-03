import sys

N = int(sys.stdin.readline())

k = 2
for i in range(N):
    k = 2*k-1

print(k**2)

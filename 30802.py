import sys
import math

N = int(sys.stdin.readline().rstrip())
sizes = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

cnt = 0
for size in sizes:
    cnt += math.ceil(size/T)

print(cnt)
print(N // P, N % P)

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

dq = deque([i+1 for i in range(N)])
res = []

for i in range(N):
    dq.rotate(-K)
    res.append(dq.pop())

print("<", end="")
print(*res, sep=", ", end="")
print(">")

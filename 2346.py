import sys
from collections import deque

N = int(sys.stdin.readline())

dq = deque(enumerate(map(int, sys.stdin.readline().split())))
res = []

for i in range(N):
    i, v = dq.popleft()
    res.append(i+1)
    if v > 0:
        dq.rotate(1-v)
    else:
        dq.rotate(-v)
      
print(*res)

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

dq = deque([x for x in range(1, N+1)])

target = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(M):
    cnt = 0
    if dq.index(target[i]) <= len(dq) - dq.index(target[i]):
        while target[i] != dq[0]:
            dq.rotate(-1)
            cnt += 1
        dq.popleft()
    else:
        while target[i] != dq[0]:
            dq.rotate(1)
            cnt += 1
        dq.popleft()
    res += cnt

print(res)

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    if N == 1:
        importance = sys.stdin.readline().rstrip()
        print(1)
    else:
        importance = deque(map(int, sys.stdin.readline().rstrip().split()))
        dq = deque([(p, i) for i, p in enumerate(importance)])
        cnt = 0
        while dq:
            if dq[0][0] == max(dq, key=lambda x: x[0])[0]:
                cnt += 1
                p, idx = dq.popleft()
                if idx == M:
                    print(cnt)
                    break
            else:
                dq.rotate(-1)

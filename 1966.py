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
        res = 0
        while M != -1:
            max_num = max(importance)
            p = importance.popleft()
            if p == max_num:
                M -= 1
                res += 1
            else:
                importance.append(p)
                if M == 0:
                    M = len(importance)-1
                else:
                    M -= 1
        print(res)

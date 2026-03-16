import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

is_queue = deque([])
for i in range(N):
    if A[i] == 0:
        is_queue.appendleft(B[i])
if M > len(is_queue):
    is_queue.extend(C[:M-len(is_queue)])
print(*list(is_queue)[:M])

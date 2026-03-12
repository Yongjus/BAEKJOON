import sys
from collections import deque

N = int(sys.stdin.readline())
if N == 1:
    a = int(sys.stdin.readline())
    if a == 1:
        print("Nice")
    else:
        print("Sad")
else:
    dq = deque(reversed(list(map(int, sys.stdin.readline().split()))))
    stack = deque([])
    for i in range(1, N+1):
        if dq and dq[-1] == i:
            dq.pop()
        elif stack and stack[-1] == i:
            stack.pop()
        elif i in dq:
            while dq[-1] != i:
                stack.append(dq.pop())
            else:
                dq.pop()
        else:
            break
    if dq or stack:
        print("Sad")
    else:
        print("Nice")

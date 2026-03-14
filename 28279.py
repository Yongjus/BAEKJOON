import sys
from collections import deque

N = int(sys.stdin.readline())

dq = deque([])
for i in range(N):
    command = sys.stdin.readline().rstrip()
    
    if command.startswith("1"):
        _, num = command.split()
        dq.appendleft(num)
    elif command.startswith("2"):
        _, num = command.split()
        dq.append(num)
    elif command == "3":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command == "4":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif command == "5":
        print(len(dq))
    elif command == "6":
        if dq:
            print(0)
        else:
            print(1)
    elif command == "7":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command == "8":
        if dq:
            print(dq[-1])
        else:
            print(-1)
    

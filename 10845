import sys

N = int(sys.stdin.readline().rstrip())

queue = []
for i in range(N):
    commend = sys.stdin.readline().rstrip()
    if commend[:4] == "push":
        _, num = commend.split()
        queue.append(int(num))
    elif commend == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif commend == "size":
        print(len(queue))
    elif commend == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif commend == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commend == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

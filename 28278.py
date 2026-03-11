import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    commend = sys.stdin.readline().rstrip()
    if commend[0] == "1":
        stack.append(commend.split()[1])
    elif commend == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif commend == "3":
        print(len(stack))
    elif commend == "4":
        if stack:
            print(0)
        else:
            print(1)
    elif commend == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)

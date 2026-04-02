import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    command = sys.stdin.readline().rstrip()
    if command.startswith("push"):
        command, num = command.split()
        stack.append(int(num))
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

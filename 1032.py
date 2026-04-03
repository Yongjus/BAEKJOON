import sys

N = int(sys.stdin.readline())

for i in range(N):
    command = list(sys.stdin.readline().rstrip())
    if i == 0:
        result = command
        n = len(result)
    else:
        for j in range(n):
            if result[j] == "?":
                continue
            elif result[j] != command[j]:
                result[j] = "?"
            else:
                pass
print(*result, sep="")

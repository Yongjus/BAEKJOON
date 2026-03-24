import sys

def star(n):
    if n == 3:
        return [["*", "*", "*"], ["*", " ", "*"], ["*", "*", "*"]]
    x = star(n//3)
    x *= 3
    for i in range(n//3):
        x[i] = x[i] * 3
    for i in range(n//3, (n//3)*2):
        x[i] = x[i] + [" "]*(n//3) + x[i]
    for i in range((n//3)*2, n):
        x[i] = x[i] * 3
    return x

N = int(sys.stdin.readline())
result = star(N)

for i in range(N):
    print(*result[i], sep="")

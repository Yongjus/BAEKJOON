import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N//5+1):
    for j in range(N//3+1):
        if N == i*5 + j*3:
            lst.append(i+j)

if lst:
    print(min(lst))
else:
    print(-1)

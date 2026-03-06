import sys

N = int(sys.stdin.readline())

lst = []
for i in range(N):
    lst.append(tuple(map(int, sys.stdin.readline().split())))

lst.sort(key=lambda x: x[1])
lst.sort(key=lambda x: x[0])

for i in lst:
    print(*i, sep=" ")

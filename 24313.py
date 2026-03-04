import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

for n in range(n0, 101):
    if int(a1*n + a0 > c*n):
        print(0)
        break
else:
    print(1)

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    b = b%4 + 4
    if a % 10 == 0:
        print(10)
    else:
        print(a**b%10)

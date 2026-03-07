import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    print(((N-1) % H + 1)*100 + ((N-1) // H + 1))

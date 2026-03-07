import sys

N, M = map(int, sys.stdin.readline().split())

set_N = set()
for i in range(N):
    set_N.add(sys.stdin.readline().rstrip())

cnt = 0
for i in range(M):
    string = sys.stdin.readline().rstrip()
    if string in set_N:
        cnt += 1

print(cnt)

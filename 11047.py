import sys

N, K = map(int, sys.stdin.readline().split())

lst = []
for _ in range(N):
    A = int(sys.stdin.readline())
    if A > K:
        continue
    else:
        lst.append(A)
cnt = 0
for l in lst[::-1]:
    if K // l:
        cnt += (K//l)
        K %= l
print(cnt)

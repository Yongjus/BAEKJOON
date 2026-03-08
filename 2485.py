import sys
import math

N = int(sys.stdin.readline())

lst = []
for i in range(N):
    tree = int(sys.stdin.readline())
    lst.append(tree)

lst_sub = [lst[i+1] - lst[i] for i in range(N-1)]

res = math.gcd(*lst_sub)

cnt = 0
for i in range(N-1):
    cnt += (lst_sub[i] // res -1)
print(cnt)



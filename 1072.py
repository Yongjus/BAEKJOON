import sys

X, Y = map(int, sys.stdin.readline().split())

Z = (100*Y)//X
# 이진 탐색
left = 0
right = X
t = X
if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left+right)//2
        if (100*(Y+mid))//(X+mid) > Z:
            t = mid
            right = mid-1
        else:
            left = mid+1
    print(t)

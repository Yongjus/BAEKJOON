import sys

X, Y = map(int, sys.stdin.readline().split())

Z = (100*Y)//X
# 이진 탐색 알고리즘
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

######################################################################
# 이진 탐색 알고리즘을 안쓰고 할 수 있을까?
import sys
import math

X, Y = map(int, sys.stdin.readline().split())

Z = (100*Y)/X
Z_0 = math.floor(Z)
Z_1 = math.ceil(Z)

if X == Y or Z_0 >= 99:
    print(-1)
elif Z_0 != Z_1:
    """
    Z = Y/X *100
    Z' = (Y+t)/(X+t) *100
    \therefore t = X*(Z'-Z)/(100-Z')  단, Z' != Z
    # Z'는 Z보다 큰 가장 작은 양의 정수 ex) Z = 54.4, Z' = 55
    """
    
    t = X*(Z_1 - Z)/(100 - Z_1)
    t = round(t, 5)  # 부동소수점 오류 해결
    print(math.ceil(t))
else:
    if math.floor((100*(Y+1))/(X+1)) != Z_0:
        # 1을 더했을 때, 변하면 1 출력
        print(1)
    else:
        # 여기서 막힘
        pass

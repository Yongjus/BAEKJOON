import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance_squared = (x2 - x1)**2 + (y2 - y1)**2
    if x1 == x2 and y1 == y2 and r1 == r2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif abs(r1 - r2)**2 < distance_squared < abs(r1 + r2)**2:
        print(2)
    elif distance_squared == abs(r1 - r2)**2 or distance_squared == abs(r1+r2)**2:
        print(1)
    else:
        print(0)

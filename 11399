import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

sum_p = 0
cumsum = []
for i in range(N):
    sum_p = sum_p + P[i]
    cumsum.append(sum_p)
print(sum(cumsum))

import sys
N, M = map(int, sys.stdin.readline().split())

set_n = set()
for i in range(N):
    set_n.add(sys.stdin.readline().rstrip())

set_m = set()
for i in range(M):
    set_m.add(sys.stdin.readline().rstrip())

result = list(set_n.intersection(set_m))
result.sort()
print(len(result))
print(*result, sep="\n")

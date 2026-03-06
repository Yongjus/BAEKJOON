import sys

N, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

# O(nlogn)
print(sorted(lst, reverse=True)[k-1])

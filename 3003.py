import sys

true = [1, 1, 2, 2, 2, 8]
lst = list(map(int, sys.stdin.readline().split()))
answer = [0, 0, 0, 0, 0, 0]
for i in range(6):
    answer[i] = true[i] - lst[i]

print(*answer)

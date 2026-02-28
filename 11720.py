import sys

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

sum = 0
for s in S:
    sum += int(s)

print(sum)

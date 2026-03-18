import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())

voca = []
for i in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        voca.append(word)

counter = Counter(voca)
result = sorted(counter, key=lambda x: (-counter[x], -len(x), x))
print(*result, sep="\n")

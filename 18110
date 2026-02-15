# python에서의 round는 오사오입이기 때문에 math.floor(n + 0.5)로 대체하여 해결할 수 있다.
import sys
import math

n = int(sys.stdin.readline())

scores = []
for i in range(n):
    scores.append(int(sys.stdin.readline().rstrip()))

trim_15 = math.floor(n*0.15 + 0.5)
scores.sort()

if scores:
    trim_scores = scores[trim_15:n-trim_15]
    print(math.floor(sum(trim_scores)/len(trim_scores) + 0.5))
else:
    print(0)

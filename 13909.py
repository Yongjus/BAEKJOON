import sys
import math

N = int(sys.stdin.readline())
print(math.floor(math.sqrt(N)))

# 규칙 발견: 제곱수에서 True, 나머지 False
# lst = [True] * (N+1)

# for i in range(2, N+1):
#     for k in range(0, N+1, i):
#         lst[k] = not lst[k]
        
# print(sum(lst[1:]))

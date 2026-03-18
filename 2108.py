import sys
import math
from collections import Counter

N = int(sys.stdin.readline())

nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
counter = Counter(nums)
max_freq = max(counter.values())
mode = [k for k, v in counter.items() if v == max_freq]

print(math.floor(sum(nums)/N + 0.5))
print(nums[N//2])
if len(mode) >= 2:
    print(mode[1])
else:
    print(mode[0])
print(max(nums) - min(nums))

import sys

mapping = {f"{i}": i for i in range(10)}
for i in range(26):
    char = chr(ord('A') + i)
    mapping[char] = 10 + i

N, B = sys.stdin.readline().split()
B = int(B)

res = 0
for i in range(len(N)-1, -1, -1):
    res = res + mapping[N[-i-1]] * (B**i)
else:
    print(res)

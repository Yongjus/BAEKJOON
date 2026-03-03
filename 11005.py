import sys

mapping = {i: f"{i}" for i in range(10)}
for i in range(26):
    mapping[10 + i] = chr(ord('A') + i)

N, B = map(int, sys.stdin.readline().split())

lst = []
while N >= B:
    lst.append(mapping[N % B])
    N = N // B
else:
    lst.append(mapping[N % B])
print(*lst[::-1], sep="")

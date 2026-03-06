import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
lst = sorted(set(numbers))
dct = {v: k for k, v in enumerate(lst)}

for i in numbers:
    print(dct[i], end=" ")

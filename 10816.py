import sys

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
need = list(map(int, sys.stdin.readline().split()))

dict_need = {}
for num in need:
    dict_need[num] = 0

for num in cards:
    if num in dict_need:
        dict_need[num] += 1

for i in need:
    print(dict_need[i], end=" ")

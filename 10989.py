import sys

N = int(sys.stdin.readline())
cnt_dict = {}
for i in range(N):
    num = int(sys.stdin.readline())
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

for i in sorted(cnt_dict.keys()):
    for j in range(cnt_dict[i]):
        print(i)

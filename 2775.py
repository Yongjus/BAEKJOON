import sys

lst = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
for i in range(1, 15):
    lst.append([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

for i in range(1, 15):
    for j in range(1, 14):
        lst[i][j] = lst[i-1][j] + lst[i][j-1]

# print(*lst, sep="\n")

T = int(sys.stdin.readline())
for t in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(lst[k][n-1])

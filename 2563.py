import sys

matrix = [False] * 10000

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    row, col = map(int, sys.stdin.readline().split())
    
    for i in range(row, min(row+10, 100)):
        for j in range(col, min(col+10, 100)):
            matrix[i+j*100] = True

print(sum(matrix))

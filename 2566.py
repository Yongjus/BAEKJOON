import sys

matrix = []
maximum = 0
max_row = 1
max_col = 1
for i in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    m = max(row)
    if maximum < m:
        maximum = m
        max_row = i + 1
        max_col = row.index(maximum) + 1

print(maximum)
print(max_row, max_col)

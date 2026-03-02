import sys

matrix = []
max_len = 1
for i in range(5):
    word = list(sys.stdin.readline().rstrip())
    matrix.append(word)
    max_len = max(max_len, len(word))

for i in range(max_len):
    for j in range(5):
        try:
            print(matrix[j][i], end="")
        except:
            pass

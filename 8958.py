import sys

N = int(sys.stdin.readline())

for i in range(N):
    OX = sys.stdin.readline().rstrip()
    score = 0
    cumul = 0
    for j in range(len(OX)):
        if OX[j] == "O":
            cumul += 1
            score += cumul
        else:
            cumul = 0
    print(score)

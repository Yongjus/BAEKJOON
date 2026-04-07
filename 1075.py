import sys

N = int(sys.stdin.readline())
N = N//100*100
F = int(sys.stdin.readline())
for i in range(0, 100):
    if (N + i) % F == 0:
        if i < 10:
            print("0"+str(i))
        else:
            print(i)
        break

import sys

L = int(sys.stdin.readline())
sentences = list(sys.stdin.readline().rstrip())

cnt = 0
for i in range(L):
    cnt = cnt + (ord(sentences[i]) - 96)*(31**i)

print(cnt % 1234567891)

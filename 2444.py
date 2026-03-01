import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    print(" "*(N-i-1), "*"*(i*2+1), sep="")

for i in range(N-2, -1, -1):
    print(" "*(N-i-1), "*"*(i*2+1), sep="")

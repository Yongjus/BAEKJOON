import sys

N = int(sys.stdin.readline())

if N == 0:
    print(1)
else:
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    print(factorial)

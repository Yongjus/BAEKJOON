import sys

fib = [0, 1]
def fibonacci(n):
    if len(fib) > n:
        return fib[n]
    else:
        fib.append(fibonacci(n-1) + fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(40)

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(fib[N-1], fib[N])

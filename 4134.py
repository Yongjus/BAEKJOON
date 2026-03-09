import sys

def is_prime(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    else:
        return True

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    if n == 0 or n == 1:
        print(2)
        continue
    while True:
        if is_prime(n):
            print(n)
            break
        n += 1

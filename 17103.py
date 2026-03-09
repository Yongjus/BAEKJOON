import sys

T = int(sys.stdin.readline())
# Initialize
N = 1000000
is_prime = [True] * (N+1)
is_prime[1] = False

# Sieve of Eratosthenes
for i in range(2, int(N**0.5)+1):
    if is_prime[i]:
        for j in range(2*i, N+1, i):
            is_prime[j] = False
primes = []
for t in range(T):
    N = int(sys.stdin.readline())
    
    if N == 4:
        print(1)
        continue

    primes = []
    for i in range(3, N//2 + 1, 2):
        if is_prime[i]:
            primes.append(i)
    cnt = 0
    for num in primes:
        if is_prime[N - num]:
            cnt += 1
    print(cnt)

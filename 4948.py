import sys

is_prime = []
while True:
    N = int(sys.stdin.readline())
    M = 2*N+1
    if N == 0:
        break
    elif M < len(is_prime):
        print(sum(is_prime[N+1:M]))
    else:
        # Initialize
        is_prime = [True] * (M+1)
        is_prime[1] = False  # 이거 빼면 틀림

        # Sieve of Eratosthenes
        for i in range(2, int(M**0.5)+1):
            if is_prime[i]:
                for j in range(2*i, M+1, i):
                    is_prime[j] = False
        
        print(sum(is_prime[N+1:M]))

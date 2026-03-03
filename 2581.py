import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime = []
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)

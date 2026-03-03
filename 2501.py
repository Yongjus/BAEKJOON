import sys

N, K = map(int, sys.stdin.readline().split())

lst = []
for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)
    
    # early stopping
    if len(lst) == K:
        print(i)
        break    

if len(lst) < K:
    print(0)

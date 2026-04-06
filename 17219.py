import sys

N, M = map(int, sys.stdin.readline().split())

idpw = dict()
for _ in range(N):
    site, pw = sys.stdin.readline().split()
    idpw[site] = pw

for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(idpw[site])
    

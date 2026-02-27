import sys

N, K = map(int, sys.stdin.readline().split())

for i in range(2**N-1):
    s = bin(i)[2:].zfill(N)
    while True:
        s_temp = s
        s = s.replace("01", "")
        if s_temp == s:
            break
    if len(s_temp) == 0:
        continue
    if K == 0:
        print(bin(i)[2:].zfill(N).replace("0", "(").replace("1", ")"))
        break
    K -= 1
else:
    print(-1)

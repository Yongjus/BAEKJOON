import sys

N = int(sys.stdin.readline().rstrip())
res = 1
while True:
    gen = res
    for n in str(gen):
        gen += int(n)
    if gen == N:
        print(res)
        break
    elif N < res:
        print(0)
        break
    else:
        res += 1

import sys

while True:
    try:
        N = int(sys.stdin.readline())
    except:
        break
    else:
        result = "-"*3**N
        for n in range(N, 0, -1):
            result = result.replace("-"*3**(n), "-"*3**(n-1)+" "*3**(n-1)+"-"*3**(n-1))
        print(result)

import sys

N = int(sys.stdin.readline())
iterable = iter(range(1, N+1))
lst = []
res = []
break_ = False
for i in range(N):
    num = int(sys.stdin.readline())
    if break_:
        continue

    if lst and num <= it:
        if num == lst[-1]:
            lst.pop()
            res.append("-")
        else:
            break_ = True
    else:
        while True:
            it = next(iterable)
            res.append("+")
            if num == it:
                res.append("-")
                break
            else:
                lst.append(it)

if break_:
    print("NO")
else:
    print(*res, sep="\n")

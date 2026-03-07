import sys

n = int(sys.stdin.readline())

recode = set()
for i in range(n):
    name, commend = sys.stdin.readline().split()
    if commend == "enter":
        recode.add(name)
    elif commend == "leave":
        recode.remove(name)

recode = sorted(recode, reverse=True)
print(*recode, sep="\n")

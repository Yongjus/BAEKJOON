import sys

S = set()

M = int(sys.stdin.readline().rstrip())

for i in range(M):
    commend = sys.stdin.readline().rstrip()
    if commend == "all" or commend == "empty":
        if commend == "all":
            S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
            # S = {x for x in range(1, 21)}
        elif commend == "empty":
            S.clear()
    else:
        commend, x = commend.split()
        x = int(x)
        if commend == "add":
            S.add(x)
        elif commend == "remove":
            S.discard(x)
        elif commend == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif commend == "toggle":
            if x in S:
                S.remove(x)
            else:
                S.add(x)

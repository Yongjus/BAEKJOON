import sys

ISBN = list(sys.stdin.readline().rstrip())

cnt = 0
for i in range(13):
    if ISBN[i] == "*":
        point = i
    else:
        if i % 2 == 0:
            cnt = cnt + int(ISBN[i])
        else:
            cnt = cnt + int(ISBN[i])*3

if point % 2 == 0:
    print((10-cnt%10)%10)
else:
    for i in range(1, 10):
        if (cnt + i*3)%10 == 0:
            print(i)
            break
    else:
        print(0)

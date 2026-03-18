import sys

N = int(sys.stdin.readline())

cnt = 0
users = set()
for i in range(N):
    user = sys.stdin.readline().rstrip()

    if user == "ENTER":
        users = set()
    elif user not in users:
        users.add(user)
        cnt += 1

print(cnt)

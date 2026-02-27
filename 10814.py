N = int(input())
user_lst = []
for i in range(N):
    user = input().split()
    user[0] = int(user[0])
    user_lst.append(user)

user_lst.sort(key=lambda x: x[0])
for i in range(N):
    print(*user_lst[i])

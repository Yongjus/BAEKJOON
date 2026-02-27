K = int(input())

lst = []
for i in range(K):
    num = int(input())
    if num == 0:
        # del lst[-1]
        lst.pop()
    else:
        lst.append(num)

print(sum(lst))

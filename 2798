N, M = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in a:
    for j in a:
        if i == j:
            continue
        for k in a:
            if k == j or k == i:
                continue
            if (M - (i+j+k) < M - sum) and (i+j+k) <= M:
                sum = i+j+k

print(sum)

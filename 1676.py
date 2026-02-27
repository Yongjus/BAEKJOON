N = int(input())

fact = 1
for i in range(1, N+1):
    fact *= i

cnt = 0
fact = str(fact)
while True:
    if fact.endswith("0"):
        cnt += 1
        fact = fact[:-1]
    else:
        print(cnt)
        break

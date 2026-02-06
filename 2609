import math
# def multiply(arr):
#     ans = 1
#     for n in arr:
#         if n == 0:
#             return 0
#         ans *= n
#     return ans

a, b = map(int, input().split())

lst_prime_factorization = []
while True:
    # if (a == 1) or (b == 1):
    #     break
    for i in range(2, max(a, b)+1):
        if (a % i == 0) and (b % i == 0):
            lst_prime_factorization.append(i)
            a = a // i
            b = b // i
            break
    else:
        gcd = multiply(lst_prime_factorization)
        gcd = math.prod(lst_prime_factorization)
        print(int(gcd))
        print(int(gcd*a*b))
        break

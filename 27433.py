import sys

def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return factorial(num-1)*num

N = int(sys.stdin.readline())

print(factorial(N))

import sys

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = a1*b2 + a2*b1
B = b1*b2
print(A//gcd(A, B), B//gcd(A, B))

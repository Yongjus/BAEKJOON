import sys

resistor = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
C = sys.stdin.readline().rstrip()

print((resistor[A]*10 + resistor[B])*10**resistor[C])

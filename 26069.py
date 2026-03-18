import sys

N = int(sys.stdin.readline())

lets_dance = set()
is_meet_ChongChong = False
for i in range(N):
    A, B = sys.stdin.readline().split()
    
    if A == "ChongChong" or B == "ChongChong":
        is_meet_ChongChong = True
        lets_dance.add(A)
        lets_dance.add(B)
    
    if is_meet_ChongChong:
        if A in lets_dance or B in lets_dance:
            lets_dance.add(A)
            lets_dance.add(B)

print(len(lets_dance))

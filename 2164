N = int(input())

cards = [i for i in range(1, N+1)]

put_under = False
while len(cards) > 1:
    if put_under:
        cards.append(cards.pop(0))
    else:
        cards.pop(0)
    put_under = not put_under
print(cards[0])

##############################################################
# deque 사용
from collections import deque

N = int(input())

cards = deque()
for i in range(1, N+1):
    cards.append(i)

put_under = False
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])

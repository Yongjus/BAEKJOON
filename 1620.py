import sys

N, M = map(int, sys.stdin.readline().split())

pokedex = {}
pokedex_num = {}
for i in range(N):
    pokemon = sys.stdin.readline().rstrip()
    pokedex[i+1] = pokemon
    pokedex_num[pokemon] = i+1

for i in range(M):
    q = sys.stdin.readline().rstrip()

    try:
        int(q)
    except ValueError:
        print(pokedex_num[q])
    else:
        print(pokedex[int(q)])

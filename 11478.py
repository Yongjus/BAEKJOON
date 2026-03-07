import sys

S = sys.stdin.readline().rstrip()

set_S = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        set_S.add(S[i:j])

print(len(set_S))

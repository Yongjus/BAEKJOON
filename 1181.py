import sys

N = int(sys.stdin.readline().rstrip())

lst = []
for i in range(N):
    word = sys.stdin.readline().rstrip()
    lst.append(word)
lst = sorted(set(lst), key=lambda x: (len(x), x))
print(*lst, sep="\n")

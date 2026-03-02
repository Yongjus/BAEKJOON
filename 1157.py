import sys
from collections import Counter

word = sys.stdin.readline().rstrip()

word = word.upper()
cnt = Counter(word)
if len(cnt) == 1:
    print(cnt.most_common(1)[0][0])
else:
    cnt = cnt.most_common(2)
    if cnt[0][1] == cnt[1][1]:
        print("?")
    else:
        print(cnt[0][0])

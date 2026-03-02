import sys

word = sys.stdin.readline().rstrip()
lst_croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0
for croatian in lst_croatian:
    if word.find(croatian) != -1:
        cnt += word.count(croatian)
        word = word.replace(croatian, ".")
print(cnt + len(word.replace(".", "")))

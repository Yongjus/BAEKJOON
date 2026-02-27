N = int(input())
for n in range(N):
    s = input()
    if s[0] == ")":
        print("NO")
        continue
    is_open = 1
    for i in range(1, len(s)):
        if s[i] == "(":
            is_open += 1
        elif is_open == 0:
            is_open = 1
            break
        else:
            is_open -= 1

    if is_open == 0:
        print("YES")
    else:
        print("NO")

import re

while True:
    sentence = input()
    if sentence[0] == ".":
        break
    s = re.sub("[A-Za-z ]", "",sentence)
    while True:
        s_temp = s
        s = s.replace("()", "")
        s = s.replace("[]", "")
        if s_temp == s:
            break
    
    if s == ".":
        print("yes")
    else:
        print("no")

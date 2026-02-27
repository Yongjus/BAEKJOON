import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == "0":
        break
    elif string == string[::-1]:
        print("yes")
    else:
        print("no")

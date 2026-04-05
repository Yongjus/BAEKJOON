import sys

is_num = False
for i in range(3):
    command = sys.stdin.readline().rstrip()
    if is_num:
        continue
    if command.isdigit():
        is_num = True
        result = int(command) + 3 - i

if result % 3 == 0 and result % 5 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)

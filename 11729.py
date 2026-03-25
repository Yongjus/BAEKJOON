import sys

start_list=[]
end_list = []

def hanoi(n, a, c):
    b = 6 - a - c
    
    if n == 1:
        start_list.append(a)
        end_list.append(c)
    else:
        hanoi(n-1, a, b)
        start_list.append(a)
        end_list.append(c)
        hanoi(n-1, b, c)

N = int(sys.stdin.readline())
hanoi(N, 1, 3)
print(len(start_list))
for start, end in zip(start_list, end_list):
    print(start, end)
    

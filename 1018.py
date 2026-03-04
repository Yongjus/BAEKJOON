import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for n in range(N):
    board.append(sys.stdin.readline().rstrip())

W = "WBWBWBWB"
B = "BWBWBWBW"
lst_res = []
for n in range(N-8+1):
    for m in range(M-8+1):
        
        cnt_w = 0
        cnt_b = 0
        for i in range(8):
            temp = board[n+i][m:m+8]
            for j in range(8):
                if i % 2 == 0:
                    if temp[j] != W[j]:
                        cnt_w += 1
                    if temp[j] != B[j]:
                        cnt_b += 1
                if i % 2 == 1:
                    if temp[j] != W[j]:
                        cnt_b += 1
                    if temp[j] != B[j]:
                        cnt_w += 1

        lst_res.append(cnt_w)
        lst_res.append(cnt_b)
print(min(lst_res))

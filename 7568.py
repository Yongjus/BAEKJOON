# 데이터 입력
N = int(input())
lst = []
for i in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp)

for i in range(N):
  k = 1
  for j in range(N):
    temp_sign = np.sign(data[i] - data[j])
    # print(temp_sign)
    if temp_sign[0] == temp_sign[1]:
        if temp_sign[0] < 0:
            k = k + 1
  print(k, end=" ")

# [Option] NumPy 사용
import numpy as np

# 데이터 변환
data = np.array(lst)

# 결과
for i in range(N):
  k = 1
  for j in range(N):
    temp_sign = np.sign(data[i] - data[j])
    # print(temp_sign)
    if temp_sign[0] == temp_sign[1]:
        if temp_sign[0] < 0:
            k = k + 1
  print(k, end=" ")


import sys
import math

def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    
def merge(A, p, q, r):
    i = p
    j = q + 1
    temp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    while i <= q:
        temp.append(A[i])
        i += 1
    while j <= r:
        temp.append(A[j])
        j += 1
    global K
    for k in range(len(temp)):
        A[p + k] = temp[k]
        K -= 1
        if K == 0:
            print(temp[k])
            return

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

merge_sort(A, 0, len(A)-1)
if K > 0:
    print(-1)

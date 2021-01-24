from collections import deque
n = int(input())
arr = deque(map(int, input().split()))
d = deque()
for i in range(n-1): #0 1 2
    for j in range(i+1, n): #1 2
        if arr[j]-arr[i]<0:
            d.append(arr[j]-arr[i])
# print(d)
print(max(d)*-1)
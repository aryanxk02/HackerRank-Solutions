n = int(input())
arr = list(map(int, input().split()))
left = []
mid = []
right = []
for i in range(n):
    if arr[i]<arr[0]:
        left.append(arr[i])
    elif arr[i]>arr[0]:
        right.append(arr[i])
    else:
        mid.append(arr[i])
print(*(left+mid+right))
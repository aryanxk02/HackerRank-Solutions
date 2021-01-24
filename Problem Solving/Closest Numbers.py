n = int(input())
arr = list(map(int, input().split()))
arr.sort()
minimum = (arr[1]-arr[0])
l = [arr[0], arr[1]]
for i in range(1, n-1):
    if arr[i+1]-arr[i] < minimum:
        l = []
        l.append(arr[i])
        l.append(arr[i+1])
        minimum = abs(arr[i+1] - arr[i])
    elif arr[i+1]-arr[i] == minimum:
        l.append(arr[i])
        l.append(arr[i+1])
print(*(l))
# 2 3 6 7
t = int(input())
for _ in range(t):
    count = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)-1):
        minimum = arr[0]
        if arr[i+1] < minimum:
            arr[i+1] = arr[i]
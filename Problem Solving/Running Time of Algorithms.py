def runningTime(arr):
    count = 0
    for i in range(n):
        for j in range(0, n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    print(count)
n = int(input())
arr = list(map(int, input().split()))
runningTime(arr)
def  jumpingOnClouds(arr):

    count = 0
    for i in range(0, n-2, 2):
        if arr[i]==1:
            i -= 1
            count += 1
        elif arr[i+2] == 0:
            count += 1
        if i == n-2:
            count += 1
            break
    print(count)

n = int(input())
arr = list(map(int, input().split()))
jumpingOnClouds(arr)
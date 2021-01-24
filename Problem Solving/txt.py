t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    last_value = arr[-1]
    for i in range(n-1, 0, -1):
        if arr[i-1]>last_value:
            arr[i]=arr[i-1]
            count += 1
        if arr[i-1]<last_value:
            arr[i]=last_value
            count += 1
            break
        # if arr[i-1]==arr[0]:
        #     arr[0]=last_value
        #     break

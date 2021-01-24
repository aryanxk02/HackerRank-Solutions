import time
start_time = time.time()
t = int(input())
x=0
while x<t:
    count = 0
    n = int(input())
    arr = list(map(int, input().split()))
    # j = 0
    for j in range(n):
        i = 0
        while i < n-1:
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
            i += 1
        j += 1
    print(count)
    x += 1
print("--- %s seconds ---" % (time.time() - start_time))


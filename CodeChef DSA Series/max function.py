t = int(input())
for i in range(t):
    n = int(input())
    final = []
    arr = list(map(int, input().split()))
    arr.sort()
    x = arr[0]  # min
    y = arr[-1] # max
    first = abs(x-y)
    for i in range(1, n):
        third = abs(arr[i]-x)
        second = abs(y-arr[i])
        final.append(first+second+third)
    print(max(final))
test = int(input())
for n in range(test):
    price = int(input())
    max_len = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, max_len):
        for j in range(i, max_len):
            if arr[i]+arr[j]==price and i!=j:
                print(i+1, j+1)
                break

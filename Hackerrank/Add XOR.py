n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if (arr[i] ^ arr[j]) % 2 == 1:
            count += 1
print(count)


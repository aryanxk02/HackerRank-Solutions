rupees = int(input())
n = int(input())
arr = list(map(int, input().split()))
count = 0

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == rupees:
            count += 1
if count == 1:
    print(True)
else:
    print(False)
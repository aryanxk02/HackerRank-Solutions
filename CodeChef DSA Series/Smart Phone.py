n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    arr.append(x)
    # print(arr)
arr.sort()
# print(arr)

final_arr = []
for i in range(len(arr)):
    count = 1
    for j in range(i+1, len(arr)):
        if arr[j] >= arr[i]:
            count = count + 1
            final_arr.append(count*arr[i])
# print(final_arr)
print(max(final_arr))


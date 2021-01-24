# x = list(map(int, input().split()))
# target = int(input())
#
# for i in range(len(x)-1):
#     for j in range(i + 1, len(x)):
#         if x[i] + x[j] == target:
#             print([i, j])

def twosum(arr, target):
    x = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]==target:
                x.append(i)
                x.append(j)
                break
    print(x)

arr = list(map(int, input().split()))
target =int(input())
twosum(arr, target)
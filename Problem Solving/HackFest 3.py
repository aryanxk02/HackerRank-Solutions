s = input()
arr = []
x = []
for i in s:
    arr.append(int(i))
for j in range(len(arr)):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
        arr[len(arr)-1] = temp
    print(arr)
    res = str("".join(map(str, arr)))
    x.append(int(res, 2))
print(x)
m = max(x)
def high(m):
    print(m&(~(m-1)))
high(m)

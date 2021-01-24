arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
l = []
for i in arr2:
    arr1.append(i)
    arr1.sort(reverse=True)
    if arr1.count(i) == 1:
        l.append(arr1.index(i)+1)
    else:
        l.append(arr1.index(i)+arr1.count(i))
    arr1.remove(i)
print(*l)
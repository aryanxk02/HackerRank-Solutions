n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
for i in range(n):
    if arr2[i] == 1:
        b1.append(arr1[i])
    elif arr2[i] == 2:
        b2.append(arr1[i])
    elif arr2[i] == 3:
        b3.append(arr1[i])
    elif arr2[i] == 4:
        b4.append(arr1[i])
    elif arr2[i] == 5:
        b5.append(arr1[i])
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

n = int(input())
arr = list(map(int, input().split()))
x = []
for i in range(len(arr)):
    count = 0
    a = []
    for j in range(i+1, len(arr)):
        if abs(arr[i]-arr[j])<=1:
            count += 1
            a.append(arr[j])
    if count > 1:
        a.append(arr[i])
    x.append(a)
for i in x:
    if abs(max(i)-min(i))<=1:
        print()
print(x)
print(max(max(x)))
# print(max(x))
# n = int(input())
# l = list(map(int, input().split()))
# m = []
# x = []
# for i in range(len(l)):
#     [m.append(l[i:j]) for j in range(i+1, len(l))]
# print(m)
# for i in m:
#     if abs(max(i)-min(i))<=1:
#         print(i)
#         x.append(len(i))
# print(max(x))
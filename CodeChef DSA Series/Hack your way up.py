n = int(input())
arr = list(map(int, input().split()))
x = []
y = []
for i in arr:
    if i > 0:
        x.append(i)
for i in range(max(x)):
    if i not in x and i != 0:
        y.append(i)
# print(x)
# print(y)
print(min(y))
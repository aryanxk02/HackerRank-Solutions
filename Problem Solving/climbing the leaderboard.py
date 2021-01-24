n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
y = a
x = []
for i in b:
    y.append(i)
    y = set(y)
    y = list(y)
    y.sort(reverse=True)
    x.append(y.index(i) + 1)
    y = a
for i in x:
    print(i)

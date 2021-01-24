n = int(input())
l = list(map(int, input().split()))

l.sort()
x = []
count = 0
for i in range(len(l)):
    a = []
    for j in range(i+1, len(l)):
        if abs(l[i]-l[j])<=1:
            count += 1
            a.append(l[j])
    if count > 1:
        a.append(l[i])
    # x.append(a)
    x.append(len(a))
print(max(x))
# print((max(x)))
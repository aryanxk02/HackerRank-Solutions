x = list(map(int, input().split()))
for i in range(len(x)):
    for j in range(len(x)-i-1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
    print(x)
print(x)
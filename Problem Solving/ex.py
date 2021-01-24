import math
a = input()
x = []
y = []
[x.append(i) for i in a]
for j in range(len(x)):
    temp = x[0]
    for i in range(len(x)-1):
        x[i] = x[i+1]
    x[len(x)-1] = temp
    res = str("".join(map(str, x)))
    y.append(int(res, 2))
m = max(y)
n = int(m)
print(int(math.log(n & (~(n - 1)), 2)))



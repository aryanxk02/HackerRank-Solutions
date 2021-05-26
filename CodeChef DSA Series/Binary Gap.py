n = int(input())
x = []
while n!=1:
    x.append(n % 2)
    n = int(n / 2)
    print(n)
x.append(1)
x.reverse()
print(x)
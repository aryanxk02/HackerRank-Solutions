n = int(input())
x = []
for i in range(1,11):
    if n%i == 0:
        x.append(i)
print(max(x))
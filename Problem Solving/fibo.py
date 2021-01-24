n = int(input())

n1, n2 = 0, 1

for i in range(n):
    sum = n1 + n2
    n1 = n2
    n2 = sum

print(sum)

# 0 1 2 3 5 8
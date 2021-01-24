n = int(input())
array = list(map(int, input().split()))
sum = 0
for i in range(0, n):
    sum = sum+array[i]
print(sum)

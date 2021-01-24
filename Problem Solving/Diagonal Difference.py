n = int(input())
count = 0
for i in range(n):
    x = list(map(int, input().split()))
    count = count + (x[i]+(-x[n-i-1]))
print(abs(count))
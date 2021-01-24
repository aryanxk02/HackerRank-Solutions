n = int(input())
sum = 0
for i in range(n):
    r = list(map(int, input().split()))
    sum = sum + r[i]-r[(n-1-i)]
    i+=1
print(abs(sum))
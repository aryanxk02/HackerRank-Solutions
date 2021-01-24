n = int(input())
r = list(map(int, input().split()))
sum1 = 0
sum2 = 0
a = 0
b = n
k=0
for i in range(0, n):
    while(k<=n):
        r = list(map(int, input().split()))
        sum1 = sum1+r[i]
        sum2 = sum2+r[i][b]
        b = b-1
        k=k+1
diff = sum1-sum2
print(abs(diff))


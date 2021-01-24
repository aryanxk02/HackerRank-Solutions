n = int(input())
a = list(map(int, input().split()))
a1 = 0
a2 = 0
a3 = 0
for i in range(0, n):
    if a[i]>0:
        a1+=1
    elif a[i]<0:
        a2+=1
    else:
        a3+=1
print(a1/n)
print(a2/n)
print(a3/n)
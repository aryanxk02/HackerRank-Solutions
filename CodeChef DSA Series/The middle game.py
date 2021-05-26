n = int(input())
length = int(input())
arr = list(map(int, input().split()))
l = []
for i in range(len(arr)):
    l.append(arr[i:n+i])
final_l = []
# l.sort()

for i in l:
    i.sort()
    if len(i)==n:
        if len(i)%2==1:
            mid = int((len(i)-1)/2)
            final_l.append(i[mid])
        elif len(i)%2==0:
            # mid = int((int((len(i)-1)/2) + int(len(i)/2))/2)
            mid = int((i[int(len(i)-1/2)] + i[int(len(i)/2)])/2)
            final_l.append(mid)


print(l)
print(*final_l)
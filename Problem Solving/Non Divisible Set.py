n, k = list(map(int, input().split()))
n = int(n)
k = int(k)
arr = list(map(int, input().split()))
l = []

for i in range(n-1):
    for j in range(i+1, n):
        if (arr[i]%k)+(arr[j]%k)!=k:
            # print(arr[i], arr[j])
            l.append(arr[i])
            l.append(arr[j])
print(len(set(l)))

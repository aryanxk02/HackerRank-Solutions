n = int(input())
array = list(map(int, input().split()))
d, m = map(int, input().split())
ans = 0

for i in range(1, m):
    if array[0]+array[i] == d:
        ans+=1
    else:
        pass

print(ans)


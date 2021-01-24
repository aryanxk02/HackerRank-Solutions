n = int(input())
socks = list(map(int, input().split()))
l = []

for i in set(socks):
    if socks.count(i)%2==1:
        l.append((socks.count(i)-1)/2)
    elif socks.count(i)%2==0:
        l.append(socks.count(i)/2)

print(int(sum(l)))

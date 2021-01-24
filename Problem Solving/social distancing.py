n = int(input())
studs = [i for i in range(1, n+1)]
m = []
dist = []
for i in range(n-1):
    x = int(input())
    # studs.append(x)
for i in range(len(studs)):
    for j in range(i+1, len(studs)):
        # a = [studs[i]]
        # a.append(studs[j])
        m.append([studs[i], studs[j]])
        # a = []
# print(m)
for i in m:
    dist.append(i[1]-i[0])
# print(dist)

total = 0
for i in dist:
    total+=i*i
print(total)
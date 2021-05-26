preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]
n = 4
count = 0
a = dict()
for i in range(len(preferences)):
    a[i] = preferences[i]

for i in pairs:
    for j in range(2):
        if j==0 and i[j+1]==a[j][0]:
            count+=1
        elif j==1 and i[j-1]==a[j][0]:
            count += 1

print(count)
print(a)
print(a[0][0])
n = int(input())
lower = [1, 2, 1]
final = []
if n==1:
    print([[1]])
elif n==2:
    print([[1], [1, 1]])
elif n==3:
    print([[1], [1, 1], [1, 2, 1]])
else:
    final = [[1], [1, 1], [1, 2, 1]]
    for i in range(n-3):
        upper = [1]
        for j in range(len(lower)-1):
            upper.append(lower[j]+lower[j+1])
        upper.append(1)
        lower = upper
        final.append(lower)
        upper = []
    print(final)

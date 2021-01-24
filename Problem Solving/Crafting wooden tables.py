req, pockets, poksize, tot = list(map(int, input().split()))
x = []
count = 0
while True:
    if tot > poksize:
        x.append(poksize)
        tot = tot - poksize
        print(x)
    else:
        x.append(tot)
        print(x)
        break
main = 0
for i in range(len(x)):
    while x[i] > 1:
        x[i] = x[i]-1
        count += 1
        if count == req:
            main += 1
            break
    if sum(x) == req:
        main += 1
        break
print(main)
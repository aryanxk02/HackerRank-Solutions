count = 0
n = 10
if n<1:
    print(0)
else:
    for i in range(2, n):
        check = True
        for j in range(2, i):
            if i%j==0:
                check=False
                break
        if check==True:
            count += 1
print(count)
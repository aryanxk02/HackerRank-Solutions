n = input()
sm1 = sum(map(int,n))

n = int(n)
sm2 = 0
i=1
while n!=1:
    i+=1
    if n%i == 0:
        n//=i
        sm2 += sum(map(int,str(i)))
        i = 1

if sm1==sm2:
    print(1)
else:
    print(0)

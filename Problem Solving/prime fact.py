n = int(input())
x = n
m = str(n)
sm2 = 0
i=1
while n!=1:
    i+=1
    if n%i == 0:
        n//=i
        sm2 += sum(map(int,str(i)))
        i = 1
m = list(map(int, m))
if sum(m)==sm2:
    print(1)
else:
    print(0)


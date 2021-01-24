d, p, q = input().split()

d = int(d)
p = int(p)
q = int(q)

ans = int()

while True:
    d=d+p
    if d==q:
        print('YES')
        break
    d=d+1
    if d==q:
        print('YES')
        break
    if d>q:
        print('NO')
        break



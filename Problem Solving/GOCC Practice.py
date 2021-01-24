t = int(input())

for _ in range(t):
    n = int(input())
    i = 1
    l = []
    # while i <= n-1:
    # # for i in range(1, n):
    #     if n % i == 0:
    #         l.append(i)
    #     i += 1
    [l.append(i) for i in range(1, n) if n%i == 0]
    if n == sum(l):
        print('YES')
    else:
        print('NO')


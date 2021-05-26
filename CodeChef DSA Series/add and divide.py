t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    a = x[0]
    b = x[1]
    count = 0
    while(a>=b):
            count += 1
            a = (a/b)
    count += 1
    print(count)

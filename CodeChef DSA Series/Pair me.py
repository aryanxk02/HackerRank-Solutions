t = int(input())
for i in range(t):
    x = list(map(int, input().split()))
    if x[0]+x[1] == x[2]:
        print("YES")
    elif x[0]+x[2] == x[1]:
        print("YES")
    elif x[1]+x[2] == x[0]:
        print("YES")
    else:
        print("NO")

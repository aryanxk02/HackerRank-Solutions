t = int(input())
for i in range(t):
    ans = []
    p = str(input()).split(':')
    print(p)

    if " AM" in p[1]:
        p = [p[0], p[1][:2]]
        print(p)
        p = int(''.join(p[:]))
        print(p)
    elif " PM" in p[0]!=12:
        p = [p[0], p[1][:2]]
        print(p)
        p = int(''.join(p[:]))
        p += 1200
        print(p)
    else:
        p = [p[0], p[1][:2]]
        p = int(''.join(p[:]))
        print(p)
    n = int(input())
    for j in range(n):
        timing = str(input()).split(" ")
        print(timing)
        x = []
        if timing[1] == "AM":
            x.append(int(timing[0].replace(':', '')))
        if timing[3] == "PM" and timing[2]!=12:
            x.append(int(timing[2].replace(':', '')))
        if timing[3] == "PM" and timing[2]==12:
            x.append(int(timing[2].replace(':', '')))
        print(x)

        if int(x[0])<=p<=int(x[1]):
            ans.append(1)
        else:
            ans.append(0)

        print(*ans)
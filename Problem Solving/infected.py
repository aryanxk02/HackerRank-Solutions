t = int(input())
x = []
count = 0
for _ in range(t):
    s = input()
    for i in range(len(s)-1):
        for j in range(i, len(s)+1):
            if len(s[i:j])>1 and s[i:j] not in x:
                x.append(s[i:j])
    print(x)
    for i in x:
        # print('i :', i)
        if i == i[::-1]:
            count+=len(i)
            print('i :',i)
print(count)
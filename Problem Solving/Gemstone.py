t = int(input())
l = []

for _ in range(t):
    s = input()
    l.append(s)
lnew = l[1:]
count = 0
print(l)
print(lnew)

for letter in l[0]:
    print('Letter :', letter)
    for string in lnew:
        print('String :', string)
        for i in range(len(lnew)):
            print('i :', i)
            if letter in lnew[i]:
                print('Letter :', letter)
                count += 1


print(count)

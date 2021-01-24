t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    flag = 0
    for letter in s1:
        if letter in s2:
            print('YES')
            flag = 1
            break
    if flag == 0:
        print('NO')

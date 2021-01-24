t = int(input())
for _ in range(t):
    # n = int(input())
    s = input()
    x = []
    [x.append(i) for i in s]

    for i in range(len(s)):
        for j in range(i+1, len(s)):

            if x[i] == x[j]:
                # print(x[i])
                # print(x[j])
                x[j] = -1
                # break
                # x.replace(x[j], '-1')
            else:
                break
    print(x.count(-1))
# n = int(input())
# s = input()
# x = []
# [x.append(i) for i in s]
# print(x)
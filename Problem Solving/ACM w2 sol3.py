# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# d = list(map(int, input().split()))
# print((a[0]*a[1])-(b[2]-b[1]+1+c[2]-c[1]+1+d[2]-d[1]+1))
# # for i in range(a[2]):
#

# a = list(map(int, input().split()))
# x = []
# for i in range(a[2]):
#     b = list(map(int, input().split()))
#     x.append(b)
# y = []
# for i in x:
#     y.append(i[2]-i[1]+1)
# # print(y)
# print((a[0]*a[1])-sum(y))
a = list(map(int, input().split()))
x = []
rows = []
for i in range(a[2]):
    a1 = list(map(int, input().split()))
    x.append([a1[1], a[2]])
    rows.append(a[0])
for 



# s = input()
# l = []
# # a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
#
# for i in s:
#     l.append(i)
# print(l)
# # import collections
# # counter=collections.Counter(l)
# # x = max(counter.values())
# # print(x)
# count = 0
# removal = 0
# for i in l:
#     maxi = l[0].count()
#     if i.count() == maxi:
#         count = 1
#     elif i.count()==maxi+1:
#         removal = 1
#         break
# 1 1 2 2
s = input()
l = []
for i in s:
    l.append(i)
import collections
counter=collections.Counter(l)
(list(counter.values())).sort(reverse=False)
print(list(counter.values()))

count = 0
removal = 0
x = min(list(counter.values()))
for i in list(counter.values()):
    if removal < 2:
        if i == x:
            count = 0
        elif i == x+1:
            removal += 1

if removal<2:
    print('YES')
else:
    print('NO')
# aaabbccdd

# s = input()
# l = []
#
# for i in s:
#     l.append(i)
# # print(l)
# # a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
# from itertools import groupby
# x = ([len(list(group)) for key, group in groupby(l)])
# if max(x) - min(x) == 0 or max(x) - min(x) == 1:
#     print('YES')
# else:
#     print('NO')
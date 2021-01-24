# arr = input()
# tn = int(arr[0])
# tq = int(arr[2])
# n = []
# q = []
# for i in range(tn):
#     we_have = list(map(int, input().split()))
#     n.append(we_have)
# for i in range(tq):
#     we_req = list(map(int, input().split()))
#     q.append(we_req)
# x = []
# for i in range(3):
#     a = []
#     [a.append(j[i]) for j in n]
#         # a.append(j[i])
#     x.append(a)
# # print(x)
# for i in q:
#     count = 0
#     for j in range(3):
#         if i[j] in x[j]:
#             count += 1
#     if count == 3:
#         print('YES')
#     else:
#         print('NO')
from collections import deque
arr = input()
tn = int(arr[0])
tq = int(arr[2])
n = deque()
q = deque()
for i in range(tn):
    we_have = list(map(int, input().split()))
    n.append(we_have)
for i in range(tq):
    we_req = list(map(int, input().split()))
    q.append(we_req)
x = deque()
for i in range(3):
    a = deque()
    [a.append(j[i]) for j in n]
        # a.append(j[i])
    x.append(a)
# print(x)
for i in q:
    count = 0
    for j in range(3):
        if i[j] in x[j]:
            count += 1
    if count == 3:
        print('YES')
    else:
        print('NO')
# import math
# t = int(input())
# for x in range(t):
#     n = int(input())
#     weights = list(map(int, input().split()))
#     lengths = list(map(int, input().split()))
#     d = {}
#     jumps = 0
#     for i in range(1, n + 1):
#         d[i] = weights.index(i)
#     for i in range(2, n + 1):
#         a = d[i]
#         b = d[i - 1]
#         temp = 0
#         if a <= b:
#             temp = (math.ceil((b + 1 - a) / lengths[a]))
#         jumps += temp
#         d[i] += temp * lengths[a]
#
#     print(jumps)
n = int(input())
weights = list(map(int, input().split()))
d = {}
jumps = 0
for i in range(1, n + 1):
    d[i] = weights.index(i)
    print(d)
print(d)
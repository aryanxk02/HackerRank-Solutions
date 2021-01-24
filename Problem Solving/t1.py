t = int(input())
while t:
    count = 0
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           count += 1
           j -= 1
        l[j+1] = key
    print(count)
    t -= 1

# t = int(input())
# while (t):
#     a = int(input())
#     b = list(map(int, input().split()))
#     c = 0
#     for i in range(1, len(b)):
#
#         key = b[i]
#         j = i - 1
#         while j >= 0 and key < b[j]:
#             b[j + 1] = b[j]
#             c += 1
#             j -= 1
#         b[j + 1] = key
#     print(c)
#     t -= 1
#
#
#
#
#

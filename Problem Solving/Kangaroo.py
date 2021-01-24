# l = list(map(int, input().split()))
#
# if l[0]<l[2] and l[1]<=l[3]:
#     print('NO')
# else:
#     while l[0]<l[2]:
#         l[0] += l[1]
#         l[2] += l[3]
#     if l[0] == l[2]:
#             print('YES')
#     else:
#             print("NO")

# def kangaroo(x1, v1, x2, v2):
    # return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'



l = list(map(int, input().split()))
# x1, v1, x2, v2
# 0   1   2   3
if (l[1]>l[3]) and ((l[2]-l[0]) % (l[3]-l[1])) == 0 :
    print('YES')
else:
    print('NO')



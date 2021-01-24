# t = int(input())
# while t>0:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(len(arr)):
#         if arr[0] == max(arr):
#             arr.remove(arr[0])
#         elif arr[-1] == max(arr):
#             arr.remove(arr[-1])
#     if arr == []:
#         print('Yes')
#     else:
#         print('No')
#     t -= 1

from _collections import deque
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     d = deque(map(int, input().split()))
#     if d[0] == max(d) or d[-1] == max(d):
#         for _ in range(n):
#             if d[0] == max(d):
#                 d.popleft()
#             elif d[-1] == max(d):
#                 d.pop()
#     if d == deque([]):
#         print('Yes')
#     else:
#         print('No')

t = int(input())
for _ in range(t):
    n = int(input())
    d = deque(map(int, input().split()))
    for _ in range(len(d)-1):
        if d[0]>=d[1]:
            d.popleft()
        elif d[-1]>=d[-2]:
            d.pop()
    # print(d)
    if len(d) == 1:
        print('Yes')
    else:
        print('No')






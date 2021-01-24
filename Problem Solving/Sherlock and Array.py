# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(0, len(arr)+1):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             print('YES')
#             break
#     else:
#         print('NO')

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    left = 0
    for i in range(n):
        # print('n=', n)
        left = left + arr[i]
        if left == total:
            print('YES')
            break
        total = total - arr[i]
    else:
        print("NO")



# def findLongestConseqSubseq(arr, n):
#     '''We insert all the array elements into unordered set.'''
#
#     S = set();
#     for i in range(n):
#         S.add(arr[i])
#
#     ans = 0
#     for i in range(n):
#
#         if S.__contains__(arr[i]):
#
#             j = arr[i]
#
#             while (S.__contains__(j)):
#                 j += 1
#
#             ans = max(ans, j - arr[i])
#     return ans
#
#
# if __name__ == '__main__':
#     arr = list(map(int, input().split()))
#     n = len(arr)
#     print(findLongestConseqSubseq(arr, n))

arr = list(map(int, input().split()))
# arr.sort()
count = 0
print(sorted(arr))
l = []
for i in range(len(arr)-2):
    if arr[i+1] - arr[i] == arr[i+2] - arr[i+1]:
        count += 1
        l.append(arr[i])

print(l)
print(count)
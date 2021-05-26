final = []

def printSubsequences(arr, index, subarr):

    if index == len(arr):
        if len(subarr) != 0:
            final.append(subarr)

    else:
        printSubsequences(arr, index + 1, subarr)
        printSubsequences(arr, index + 1, subarr + [arr[index]])


# def pairORSum(arr, n):
#     ans = 0
#     for i in range(0, n):
#         for j in range(i + 1, n):
#             ans = ans + (arr[i] ^ arr[j])
#     return ans

arr = list(map(int, input().split()))
printSubsequences(arr, 0, [])
final.sort()
print(final)

count = 0
final2 = []
for i in range(0, len(final)):
    if len(final[i])>1:
        final2.append(final[i])
for i in (final2):
    for j in range(0, len(i)):
        for k in range(j+1, len(i)):
            count += i[j]^i[k]
count1 = 0
for i in final:
    if len(i) == 1:
        count1 += sum(i)
print(final2)
print(count+count1)
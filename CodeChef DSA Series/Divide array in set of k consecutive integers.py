nums = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8]
k = 4
max_k = 0
x = []
repeated = []
nums.sort()
# print(nums)

for i in nums:
    if max_k>=4:
        if len(x) != k:
            if i not in x:
                x.append(i)
            else:
                # rep_occ += 1
                repeated.append(i)
        else:
            max_k += k
            x = []
if max_k == k:
    print("YES")
else:
    print("NO")
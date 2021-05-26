nums1 = [1,2,2,1]
nums2 = [2,2]

x = []

nums1 = list(set(nums1))
nums2 = list(set(nums2))

nums1 = nums1 + nums2

nums1.sort()
print(nums1)
for i in range(1, len(nums1)):
    if nums1[i] == nums1[i-1]:
        x.append(nums1[i])

print(x)
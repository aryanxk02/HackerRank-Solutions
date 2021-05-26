nums = [3,2,3,1,2,4,5,5,6]
k = 4

nums = set(nums)
nums = list(nums)

nums.sort()
print(nums)
print(nums[-k])
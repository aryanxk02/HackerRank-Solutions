nums= [1,2]

nums = set(nums)
nums = list(nums)
nums.remove(max(nums))
nums.remove(max(nums))

print(max(nums))
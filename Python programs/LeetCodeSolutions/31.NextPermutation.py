# 31. Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
#
# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]
#
# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100

def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = reversed(nums[i+1:])
    return nums

# Example usage
nums = [1,2,3]
print("Next permutation:", nextPermutation(nums))  # Output: [1,3,2]

"""
LeetCode 2191. Sort the Jumbled Numbers

Given an array mapping and an array nums, sort nums according to the new values obtained by mapping each digit using mapping.

Example:
Input: mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]
Output: [338,38,991]

Constraints:
- mapping.length == 10
- 0 <= nums.length <= 10^5
- 0 <= nums[i] < 10^9
"""

def sortJumbled(mapping, nums):
    def mapped(x):
        return int(''.join(str(mapping[int(d)]) for d in str(x)))
    return sorted(nums, key=lambda x: (mapped(x), nums.index(x)))

# Example usage:
# print(sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))  # Output: [338,38,991]

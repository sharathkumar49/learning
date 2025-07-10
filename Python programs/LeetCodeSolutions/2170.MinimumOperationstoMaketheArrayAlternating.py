"""
LeetCode 2170. Minimum Operations to Make the Array Alternating

Given an array nums, return the minimum number of operations to make the array alternating (nums[i] != nums[i+1]).

Example:
Input: nums = [3,1,3,2,4,3]
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def minimumOperations(nums):
    from collections import Counter
    even = Counter(nums[::2])
    odd = Counter(nums[1::2])
    e1, e2 = even.most_common(2) + [(None,0)]*2
    o1, o2 = odd.most_common(2) + [(None,0)]*2
    if e1[0] != o1[0]:
        return len(nums) - e1[1] - o1[1]
    return len(nums) - max(e1[1]+o2[1], e2[1]+o1[1])

# Example usage:
# print(minimumOperations([3,1,3,2,4,3]))  # Output: 3

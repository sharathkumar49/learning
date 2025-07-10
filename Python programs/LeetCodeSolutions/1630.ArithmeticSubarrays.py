"""
LeetCode 1630. Arithmetic Subarrays

Given an array nums and a list of queries, return a list of booleans where each element is true if the subarray can be rearranged to form an arithmetic sequence.

Example 1:
Input: nums = [4,6,5,9,3,7], l = [0,2,2], r = [2,5,5]
Output: [true,false,true]

Constraints:
- 2 <= nums.length <= 500
- 1 <= nums[i] <= 10^5
- 1 <= l.length == r.length <= 500
"""

def checkArithmeticSubarrays(nums, l, r):
    res = []
    for a, b in zip(l, r):
        arr = sorted(nums[a:b+1])
        d = arr[1] - arr[0]
        ok = all(arr[i] - arr[i-1] == d for i in range(2, len(arr)))
        res.append(ok)
    return res

# Example usage:
# nums = [4,6,5,9,3,7]
# l = [0,2,2]
# r = [2,5,5]
# print(checkArithmeticSubarrays(nums, l, r))  # Output: [True, False, True]

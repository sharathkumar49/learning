"""
LeetCode 1775. Equal Sum Arrays With Minimum Number of Operations

Given two arrays nums1 and nums2, return the minimum number of operations to make their sums equal, or -1 if impossible.

Example 1:
Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 1 <= nums1[i], nums2[i] <= 6
"""

def minOperations(nums1, nums2):
    from collections import Counter
    if sum(nums1) < sum(nums2):
        nums1, nums2 = nums2, nums1
    diff = sum(nums1) - sum(nums2)
    if diff == 0:
        return 0
    count = [0]*6
    for x in nums1:
        count[x-1] += 1
    for x in nums2:
        count[6-x] += 1
    ops = 0
    for i in range(5, 0, -1):
        while count[i] and diff > 0:
            take = min(count[i], (diff + i - 1)//i)
            diff -= take * i
            ops += take
            count[i] -= take
    return ops if diff <= 0 else -1

# Example usage:
# nums1 = [1,2,3,4,5,6]
# nums2 = [1,1,2,2,2,2]
# print(minOperations(nums1, nums2))  # Output: 3

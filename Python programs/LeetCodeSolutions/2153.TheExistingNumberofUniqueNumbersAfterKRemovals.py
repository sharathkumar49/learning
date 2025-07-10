"""
LeetCode 2153. The Existing Number of Unique Numbers After K Removals

Given an integer array nums and an integer k, return the number of unique integers left in the array after removing exactly k elements.

Example:
Input: nums = [5,5,4], k = 1
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length
- 1 <= nums[i] <= 10^9
"""

def findLeastNumOfUniqueInts(nums, k):
    from collections import Counter
    c = Counter(nums)
    arr = sorted(c.values())
    res = len(arr)
    for v in arr:
        if k >= v:
            k -= v
            res -= 1
        else:
            break
    return res

# Example usage:
# print(findLeastNumOfUniqueInts([5,5,4], 1))  # Output: 1

"""
220. Contains Duplicate III
https://leetcode.com/problems/contains-duplicate-iii/

Given an integer array nums and two integers k and t, return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^4
- 0 <= t <= 2^31 - 1

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""
def containsNearbyAlmostDuplicate(nums, k, t):
    if t < 0:
        return False
    bucket = {}
    w = t + 1
    for i, num in enumerate(nums):
        m = num // w
        if m in bucket:
            return True
        if m - 1 in bucket and abs(num - bucket[m - 1]) < w:
            return True
        if m + 1 in bucket and abs(num - bucket[m + 1]) < w:
            return True
        bucket[m] = num
        if i >= k:
            del bucket[nums[i - k] // w]
    return False

# Example usage:
if __name__ == "__main__":
    print(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))        # Output: True
    print(containsNearbyAlmostDuplicate([1,0,1,1], 1, 2))       # Output: True
    print(containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))   # Output: False

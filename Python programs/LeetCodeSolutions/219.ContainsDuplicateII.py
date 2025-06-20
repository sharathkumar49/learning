"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
def containsNearbyDuplicate(nums, k):
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    return False

# Example usage:
if __name__ == "__main__":
    print(containsNearbyDuplicate([1,2,3,1], 3))        # Output: True
    print(containsNearbyDuplicate([1,0,1,1], 1))       # Output: True
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))   # Output: False

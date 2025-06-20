"""
259. 3Sum Smaller
https://leetcode.com/problems/3sum-smaller/

Given an array of n integers nums and an integer target, return the number of index triplets i, j, k with 0 <= i < j < k < n such that nums[i] + nums[j] + nums[k] < target.

Constraints:
- 3 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- -1000 <= target <= 1000

Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
"""
def threeSumSmaller(nums, target):
    nums.sort()
    n = len(nums)
    count = 0
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count

# Example usage:
if __name__ == "__main__":
    print(threeSumSmaller([-2,0,1,3], 2))  # Output: 2
    print(threeSumSmaller([], 0))          # Output: 0
    print(threeSumSmaller([0], 0))        # Output: 0

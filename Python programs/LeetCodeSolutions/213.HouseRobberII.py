"""
213. House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums, return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Example 1:
Input: nums = [2,3,2]
Output: 3

Example 2:
Input: nums = [1,2,3,1]
Output: 4

Example 3:
Input: nums = [1,2,3]
Output: 3
"""
def rob(nums):
    def rob_linear(nums):
        prev = curr = 0
        for n in nums:
            prev, curr = curr, max(curr, prev + n)
        return curr
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

# Example usage:
if __name__ == "__main__":
    print(rob([2,3,2]))      # Output: 3
    print(rob([1,2,3,1]))   # Output: 4
    print(rob([1,2,3]))     # Output: 3

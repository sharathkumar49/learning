"""
LeetCode 698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1,4), (2,3), (2,3) with equal sum.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
- 1 <= k <= len(nums) <= 16
- 0 <= nums[i] < 10000
"""
from typing import List

def canPartitionKSubsets(nums: List[int], k: int) -> bool:
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k
    nums.sort(reverse=True)
    used = [False] * len(nums)
    def dfs(k, start, curr_sum):
        if k == 1:
            return True
        if curr_sum == target:
            return dfs(k-1, 0, 0)
        for i in range(start, len(nums)):
            if not used[i] and curr_sum + nums[i] <= target:
                used[i] = True
                if dfs(k, i+1, curr_sum + nums[i]):
                    return True
                used[i] = False
        return False
    return dfs(k, 0, 0)

# Example usage
if __name__ == "__main__":
    print(canPartitionKSubsets([4,3,2,3,5,2,1], 4))  # Output: True
    print(canPartitionKSubsets([1,2,3,4], 3))        # Output: False

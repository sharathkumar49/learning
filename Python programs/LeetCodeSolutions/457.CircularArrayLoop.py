"""
457. Circular Array Loop

Given a circular array nums, return true if there is a cycle in the array.
A cycle must start and end at the same index and the cycle's length > 1. The movement is determined by the value at each index.

Constraints:
- 1 <= nums.length <= 5000
- -1000 <= nums[i] <= 1000
- nums[i] != 0

Example:
Input: nums = [2,-1,1,2,2]
Output: True
"""

class Solution:
    def circularArrayLoop(self, nums: list) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            slow, fast = i, i
            while True:
                slow = (slow + nums[slow]) % n
                fast = (fast + nums[fast]) % n
                fast = (fast + nums[fast]) % n
                if nums[slow] * nums[i] <= 0 or nums[fast] * nums[i] <= 0:
                    break
                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True
            j = i
            val = nums[i]
            while nums[j] * val > 0:
                next_j = (j + nums[j]) % n
                nums[j] = 0
                j = next_j
        return False

# Example usage:
sol = Solution()
print(sol.circularArrayLoop([2,-1,1,2,2]))  # Output: True

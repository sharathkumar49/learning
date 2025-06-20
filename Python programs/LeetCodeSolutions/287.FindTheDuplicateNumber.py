"""
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive, return the duplicate number.

Constraints:
- 1 <= n <= 10^5
- 1 <= nums[i] <= n
- There is only one repeated number in nums, but it could be repeated more than once.
- You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
"""
def findDuplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow

# Example usage:
if __name__ == "__main__":
    print(findDuplicate([1,3,4,2,2]))  # Output: 2
    print(findDuplicate([3,1,3,4,2])) # Output: 3

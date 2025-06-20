"""
665. Non-decreasing Array
Difficulty: Medium

Given an array nums with n integers, check if it could become non-decreasing by modifying at most one element.

Example 1:
Input: nums = [4,2,3]
Output: true

Example 2:
Input: nums = [4,2,1]
Output: false

Constraints:
1 <= n <= 10^4
-10^5 <= nums[i] <= 10^5
"""

def checkPossibility(nums):
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            cnt += 1
            if cnt > 1:
                return False
            if i == 1 or nums[i] >= nums[i-2]:
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
    return True

# Example usage
if __name__ == "__main__":
    print(checkPossibility([4,2,3]))  # Output: True
    print(checkPossibility([4,2,1]))  # Output: False

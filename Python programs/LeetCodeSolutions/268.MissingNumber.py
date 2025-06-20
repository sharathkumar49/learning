"""
268. Missing Number
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

# Example usage:
if __name__ == "__main__":
    print(missingNumber([3,0,1]))           # Output: 2
    print(missingNumber([0,1]))             # Output: 2
    print(missingNumber([9,6,4,2,3,5,7,0,1])) # Output: 8

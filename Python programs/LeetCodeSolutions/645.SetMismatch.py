"""
645. Set Mismatch
Difficulty: Easy

You have a set of numbers from 1 to n. Some numbers are missing and some numbers are duplicated. Return the duplicate and the missing number as an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Constraints:
2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""

def findErrorNums(nums):
    n = len(nums)
    s = set(nums)
    return [sum(nums) - sum(s), sum(range(1, n+1)) - sum(s)]

# Example usage
if __name__ == "__main__":
    print(findErrorNums([1,2,2,4]))  # Output: [2,3]

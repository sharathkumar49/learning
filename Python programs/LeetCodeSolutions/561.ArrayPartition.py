"""
561. Array Partition
Difficulty: Easy

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the order of elements) are:
1. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
2. (1, 3), (2, 4) -> 1 + 2 = 3
3. (1, 4), (2, 3) -> 1 + 2 = 3
So the maximum possible sum is 4.

Constraints:
1 <= n <= 10^4
-10^4 <= nums[i] <= 10^4
nums.length == 2 * n
"""

def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])

# Example usage
if __name__ == "__main__":
    print(arrayPairSum([1,4,3,2]))  # Output: 4

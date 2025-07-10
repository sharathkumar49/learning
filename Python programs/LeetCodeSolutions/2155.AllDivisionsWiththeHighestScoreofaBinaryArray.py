"""
LeetCode 2155. All Divisions With the Highest Score of a Binary Array

Given a binary array nums, for each index i, the division score is the number of 0's in the left part plus the number of 1's in the right part. Return all indices with the highest score.

Example:
Input: nums = [0,0,1,0]
Output: [2,4]

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
"""

def maxScoreIndices(nums):
    n = len(nums)
    left_zeros = 0
    right_ones = sum(nums)
    scores = [left_zeros + right_ones]
    for i in range(n):
        if nums[i] == 0:
            left_zeros += 1
        else:
            right_ones -= 1
        scores.append(left_zeros + right_ones)
    mx = max(scores)
    return [i for i, v in enumerate(scores) if v == mx]

# Example usage:
# print(maxScoreIndices([0,0,1,0]))  # Output: [2,4]

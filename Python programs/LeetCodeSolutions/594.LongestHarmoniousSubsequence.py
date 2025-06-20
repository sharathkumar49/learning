"""
594. Longest Harmonious Subsequence
Difficulty: Easy

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A harmonious subsequence is one where the difference between its maximum value and minimum value is exactly 1.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Constraints:
1 <= nums.length <= 2 * 10^4
-10^9 <= nums[i] <= 10^9
"""

def findLHS(nums):
    from collections import Counter
    count = Counter(nums)
    res = 0
    for x in count:
        if x+1 in count:
            res = max(res, count[x] + count[x+1])
    return res

# Example usage
if __name__ == "__main__":
    print(findLHS([1,3,2,2,5,2,3,7]))  # Output: 5
    print(findLHS([1,2,3,4]))          # Output: 2

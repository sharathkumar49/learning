"""
LeetCode 740. Delete and Earn

You are given an integer array nums. You can perform the following operation as many times as you like:
- Pick any nums[i] and delete it to earn nums[i] points. Afterward, you must delete every element equal to nums[i] - 1 and nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation.

Example 1:
Input: nums = [3,4,2]
Output: 6

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 10^4
"""
from typing import List

def deleteAndEarn(nums: List[int]) -> int:
    from collections import Counter
    count = Counter(nums)
    nums = sorted(set(nums))
    earn1 = earn2 = 0
    prev = None
    for n in nums:
        curr = n * count[n]
        if prev is not None and n == prev + 1:
            earn1, earn2 = earn2, max(earn1 + curr, earn2)
        else:
            earn1, earn2 = earn2, earn2 + curr
        prev = n
    return earn2

# Example usage
if __name__ == "__main__":
    print(deleteAndEarn([3,4,2]))      # Output: 6
    print(deleteAndEarn([2,2,3,3,3,4]))  # Output: 9

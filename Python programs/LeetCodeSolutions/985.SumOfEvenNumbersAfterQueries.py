"""
985. Sum of Even Numbers After Queries
https://leetcode.com/problems/sum-of-even-numbers-after-queries/

Given an integer array nums and an array queries where queries[i] = [val, index], for each query, add val to nums[index], then return the sum of the even values of nums after each query.

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= queries.length <= 10^4
- -10^4 <= nums[i], val <= 10^4
- 0 <= index < nums.length

Example:
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
"""
from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = sum(x for x in nums if x % 2 == 0)
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            res.append(even_sum)
        return res

# Example usage
if __name__ == "__main__":
    nums = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    print(Solution().sumEvenAfterQueries(nums, queries))  # Output: [8,6,2,4]

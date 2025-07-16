"""
LeetCode 2343. Query Kth Smallest Trimmed Number

Given nums and queries, return the kth smallest trimmed number for each query.

Example:
Input: nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]
Output: [2,2,1,0]

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i].length <= 100
"""

def smallestTrimmedNumbers(nums, queries):
    res = []
    for k, trim in queries:
        trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
        trimmed.sort()
        res.append(trimmed[k-1][1])
    return res

# Example usage:
# print(smallestTrimmedNumbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]))  # Output: [2,2,1,0]

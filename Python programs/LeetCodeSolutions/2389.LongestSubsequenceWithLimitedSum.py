"""
LeetCode 2389. Longest Subsequence With Limited Sum

Given an array and queries, return the length of the longest subsequence with sum <= query for each query.

Constraints:
- 1 <= nums.length, queries.length <= 10^3
"""

def answerQueries(nums, queries):
    nums.sort()
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1]+num)
    res = []
    for q in queries:
        l, r = 0, len(prefix)-1
        while l < r:
            m = (l+r)//2
            if prefix[m] > q:
                r = m
            else:
                l = m+1
        res.append(l-1)
    return res

# Example usage:
# print(answerQueries([4,5,2,1],[3,10,21]))  # Output: [2,3,4]

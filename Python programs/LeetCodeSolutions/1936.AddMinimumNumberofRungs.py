"""
LeetCode 1936. Add Minimum Number of Rungs

Given an array rungs and an integer dist, return the minimum number of rungs to add to climb to the last rung.

Example:
Input: rungs = [1,3,5,10], dist = 2
Output: 2

Constraints:
- 1 <= rungs.length <= 10^5
- 1 <= rungs[i] <= 10^9
- 1 <= dist <= 10^9
"""

def addRungs(rungs, dist):
    prev = 0
    res = 0
    for r in rungs:
        if r - prev > dist:
            res += (r - prev - 1) // dist
        prev = r
    return res

# Example usage:
# print(addRungs([1,3,5,10], 2))  # Output: 2

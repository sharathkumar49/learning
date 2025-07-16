"""
LeetCode 2237. Count Positions on Street With Required Brightness

Given n, lights, and requirement, return the number of positions with required brightness.

Example:
Input: n = 5, lights = [[1,2],[3,1]], requirement = [1,2,1,2,1]
Output: 5

Constraints:
- 1 <= n <= 10^5
- 1 <= lights.length <= 10^5
"""

def meetRequirement(n, lights, requirement):
    diff = [0]*(n+2)
    for pos, r in lights:
        diff[max(1,pos-r)] += 1
        diff[min(n,pos+r)+1] -= 1
    curr = 0
    res = 0
    for i in range(1, n+1):
        curr += diff[i]
        if curr >= requirement[i-1]:
            res += 1
    return res

# Example usage:
# print(meetRequirement(5, [[1,2],[3,1]], [1,2,1,2,1]))  # Output: 5

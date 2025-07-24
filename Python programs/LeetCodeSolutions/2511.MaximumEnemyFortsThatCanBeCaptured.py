"""
LeetCode 2511. Maximum Enemy Forts That Can Be Captured

Given a list of forts, return the maximum number of enemy forts that can be captured.

Constraints:
- 1 <= forts.length <= 10^5
"""

def captureForts(forts):
    res = 0
    last = -1
    for i, f in enumerate(forts):
        if f == 1 or f == -1:
            if last != -1 and forts[last] + f == 0:
                res = max(res, i - last - 1)
            last = i
    return res
# Example usage:
# print(captureForts([1,0,0,-1,0,0,0,0,1]))  # Output: 4

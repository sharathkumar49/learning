"""
LeetCode 2106. Maximum Fruits Harvested After at Most K Steps

Given fruits at positions, return the maximum number of fruits that can be collected in at most k steps.

Example:
Input: fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
Output: 9

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= startPos, k <= 2 * 10^5
- 0 <= fruits[i][0] <= 2 * 10^5
- 0 <= fruits[i][1] <= 10^5
"""

def maxTotalFruits(fruits, startPos, k):
    n = len(fruits)
    pos = [x for x, _ in fruits]
    amount = [y for _, y in fruits]
    import bisect
    prefix = [0]
    for a in amount:
        prefix.append(prefix[-1] + a)
    res = 0
    for l in range(n):
        for r in range(l, n):
            left = pos[l]
            right = pos[r]
            if abs(startPos - left) + (right - left) <= k or abs(startPos - right) + (right - left) <= k:
                res = max(res, prefix[r+1] - prefix[l])
    return res

# Example usage:
# print(maxTotalFruits([[2,8],[6,3],[8,6]], 5, 4))  # Output: 9

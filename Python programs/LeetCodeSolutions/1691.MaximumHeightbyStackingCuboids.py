"""
LeetCode 1691. Maximum Height by Stacking Cuboids

Given n cuboids, return the maximum height by stacking them.

Example 1:
Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
Output: 190

Constraints:
- 1 <= cuboids.length <= 100
- 1 <= widthi, lengthi, heighti <= 100
"""

def maxHeight(cuboids):
    for c in cuboids:
        c.sort()
    cuboids.sort()
    n = len(cuboids)
    dp = [0]*n
    for i in range(n):
        dp[i] = cuboids[i][2]
        for j in range(i):
            if all(cuboids[j][k] <= cuboids[i][k] for k in range(3)):
                dp[i] = max(dp[i], dp[j] + cuboids[i][2])
    return max(dp)

# Example usage:
# cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# print(maxHeight(cuboids))  # Output: 190

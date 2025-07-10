"""
LeetCode 2209. Minimum White Tiles After Covering With Carpets

Given a 0-indexed string floor of black ('0') and white ('1') tiles, and integers numCarpets and carpetLen, return the minimum number of white tiles still visible after covering some tiles with numCarpets black carpets of length carpetLen each.

Example:
Input: floor = "10110101", numCarpets = 2, carpetLen = 2
Output: 2

Constraints:
- 1 <= carpetLen <= floor.length <= 1000
- floor[i] is '0' or '1'
- 1 <= numCarpets <= 1000
"""

def minimumWhiteTiles(floor, numCarpets, carpetLen):
    n = len(floor)
    dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]
    
    # Precompute suffix sums of white tiles
    white = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        white[i] = white[i+1] + int(floor[i])
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][0] + int(floor[i-1])
        for j in range(1, numCarpets + 1):
            # Either don't use carpet at i
            dp[i][j] = dp[i-1][j] + int(floor[i-1])
            # Or use carpet at i
            if i >= carpetLen:
                dp[i][j] = min(dp[i][j], dp[i-carpetLen][j-1])
    
    return dp[n][numCarpets]

# Example usage:
# print(minimumWhiteTiles("10110101", 2, 2))  # Output: 2

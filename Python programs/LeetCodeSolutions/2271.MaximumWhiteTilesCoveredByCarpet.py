"""
LeetCode 2271. Maximum White Tiles Covered by a Carpet

Given tiles and carpetLen, return the maximum number of white tiles covered by the carpet.

Example:
Input: tiles = [[1,5],[10,11],[12,18]], carpetLen = 5
Output: 5

Constraints:
- 1 <= tiles.length <= 10^5
- 1 <= carpetLen <= 10^9
"""

def maximumWhiteTiles(tiles, carpetLen):
    tiles.sort()
    n = len(tiles)
    res = 0
    j = 0
    cover = 0
    for i in range(n):
        start = tiles[i][0]
        end = start + carpetLen - 1
        while j < n and tiles[j][1] <= end:
            cover += tiles[j][1] - tiles[j][0] + 1
            j += 1
        if j < n and tiles[j][0] <= end:
            cover += end - tiles[j][0] + 1
        res = max(res, cover)
        cover -= tiles[i][1] - tiles[i][0] + 1
    return res

# Example usage:
# print(maximumWhiteTiles([[1,5],[10,11],[12,18]], 5))  # Output: 5

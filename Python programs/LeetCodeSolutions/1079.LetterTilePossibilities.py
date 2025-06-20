"""
1079. Letter Tile Possibilities

You have a set of tiles, each tile has a letter on it. Return the number of possible non-empty sequences of letters you can make.

Constraints:
- 1 <= tiles.length <= 7
- tiles consists of uppercase English letters.

Example:
Input: tiles = "AAB"
Output: 8
"""
def numTilePossibilities(tiles: str) -> int:
    from collections import Counter
    def dfs(counter):
        res = 0
        for c in counter:
            if counter[c] > 0:
                res += 1
                counter[c] -= 1
                res += dfs(counter)
                counter[c] += 1
        return res
    return dfs(Counter(tiles))

# Example usage:
tiles = "AAB"
print(numTilePossibilities(tiles))  # Output: 8

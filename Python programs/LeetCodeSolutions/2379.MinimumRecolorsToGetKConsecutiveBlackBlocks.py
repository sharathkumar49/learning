"""
LeetCode 2379. Minimum Recolors to Get K Consecutive Black Blocks

Given a string blocks, return the minimum recolors to get k consecutive 'B'.

Constraints:
- 1 <= blocks.length <= 100
- 1 <= k <= blocks.length
"""

def minimumRecolors(blocks, k):
    min_recolors = float('inf')
    for i in range(len(blocks)-k+1):
        min_recolors = min(min_recolors, blocks[i:i+k].count('W'))
    return min_recolors

# Example usage:
# print(minimumRecolors("WBBWWBBWBW", 7))  # Output: 3

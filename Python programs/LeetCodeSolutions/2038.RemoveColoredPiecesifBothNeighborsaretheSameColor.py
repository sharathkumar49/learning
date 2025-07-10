"""
LeetCode 2038. Remove Colored Pieces if Both Neighbors are the Same Color

Given a string colors, return true if Alice wins the game, false otherwise.

Example:
Input: colors = "AAABABB"
Output: true

Constraints:
- 1 <= colors.length <= 10^5
- colors consists only of 'A' and 'B'
"""

def winnerOfGame(colors):
    a = b = 0
    for i in range(1, len(colors)-1):
        if colors[i-1] == colors[i] == colors[i+1]:
            if colors[i] == 'A':
                a += 1
            else:
                b += 1
    return a > b

# Example usage:
# print(winnerOfGame("AAABABB"))  # Output: True

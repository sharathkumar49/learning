"""
LeetCode 2214. Minimum Health to Beat Game

Given an array damage, return the minimum health required to beat the game.

Example:
Input: damage = [2,7,4,3]
Output: 17

Constraints:
- 1 <= damage.length <= 10^5
- 1 <= damage[i] <= 10^5
"""

def minimumHealth(damage):
    total = sum(damage)
    max_damage = max(damage)
    return total - max_damage + 1

# Example usage:
# print(minimumHealth([2,7,4,3]))  # Output: 17

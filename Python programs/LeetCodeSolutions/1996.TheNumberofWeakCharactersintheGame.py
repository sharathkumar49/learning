"""
LeetCode 1996. The Number of Weak Characters in the Game

Given a list of characters with attack and defense, return the number of weak characters.

Example:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0

Constraints:
- 2 <= properties.length <= 10^5
- properties[i].length == 2
- 1 <= attack_i, defense_i <= 10^5
"""

def numberOfWeakCharacters(properties):
    properties.sort(key=lambda x: (-x[0], x[1]))
    max_def = 0
    res = 0
    for _, d in properties:
        if d < max_def:
            res += 1
        else:
            max_def = d
    return res

# Example usage:
# print(numberOfWeakCharacters([[5,5],[6,3],[3,6]]))  # Output: 0

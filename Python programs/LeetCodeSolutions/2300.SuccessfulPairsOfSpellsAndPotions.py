"""
LeetCode 2300. Successful Pairs of Spells and Potions

Given spells, potions, and success, return the number of successful pairs for each spell.

Example:
Input: spells = [10,11,12], potions = [1,2,3], success = 10
Output: [3,3,3]

Constraints:
- 1 <= spells.length, potions.length <= 10^5
- 1 <= success <= 10^10
"""

def successfulPairs(spells, potions, success):
    potions.sort()
    res = []
    n = len(potions)
    for spell in spells:
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if spell * potions[mid] >= success:
                right = mid
            else:
                left = mid + 1
        res.append(n - left)
    return res

# Example usage:
# print(successfulPairs([10,11,12], [1,2,3], 10))  # Output: [3,3,3]

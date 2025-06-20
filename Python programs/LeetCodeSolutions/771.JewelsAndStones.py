"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters.
- All the characters of jewels are unique.
"""
def numJewelsInStones(jewels, stones):
    jewel_set = set(jewels)
    return sum(s in jewel_set for s in stones)

# Example usage:
print(numJewelsInStones("aA", "aAAbbbb"))  # Output: 3
print(numJewelsInStones("z", "ZZ"))        # Output: 0

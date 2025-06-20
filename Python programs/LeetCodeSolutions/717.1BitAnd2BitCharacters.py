"""
LeetCode 717. 1-bit and 2-bit Characters

We have two special characters:
- The first character can be represented by one bit 0.
- The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:
Input: bits = [1,0,0]
Output: true

Example 2:
Input: bits = [1,1,1,0]
Output: false

Constraints:
- 1 <= bits.length <= 1000
- bits[i] is either 0 or 1.
"""
from typing import List

def isOneBitCharacter(bits: List[int]) -> bool:
    i = 0
    n = len(bits)
    while i < n - 1:
        if bits[i] == 1:
            i += 2
        else:
            i += 1
    return i == n - 1

# Example usage
if __name__ == "__main__":
    print(isOneBitCharacter([1,0,0]))    # Output: True
    print(isOneBitCharacter([1,1,1,0]))  # Output: False

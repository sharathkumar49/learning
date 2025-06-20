"""
914. X of a Kind in a Deck of Cards
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

Given an integer array deck where deck[i] represents the number written on the ith card, return true if and only if you can group the cards into one or more groups of size x, where x >= 2, and every group has the same integer.

Constraints:
- 1 <= deck.length <= 10^4
- 0 <= deck[i] < 10^4

Example:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
"""
from typing import List
from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = Counter(deck).values()
        return reduce(gcd, vals) >= 2

# Example usage
if __name__ == "__main__":
    deck = [1,2,3,4,4,3,2,1]
    print(Solution().hasGroupsSizeX(deck))  # Output: True

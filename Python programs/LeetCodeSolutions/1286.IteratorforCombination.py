"""
LeetCode 1286. Iterator for Combination

Design an iterator that returns the combinations of a given string characters of length combinationLength in lexicographical order.

Constraints:
- 1 <= combinationLength <= characters.length <= 15
- characters consists of lowercase English letters only.

Example:
Input: characters = "abc", combinationLength = 2
Output: ["ab","ac","bc"]
"""
from itertools import combinations
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combos = ["".join(c) for c in combinations(characters, combinationLength)]
        self.index = 0
    def next(self) -> str:
        res = self.combos[self.index]
        self.index += 1
        return res
    def hasNext(self) -> bool:
        return self.index < len(self.combos)

# Example usage:
# iterator = CombinationIterator("abc", 2)
# print(iterator.next())    # Output: "ab"
# print(iterator.hasNext()) # Output: True

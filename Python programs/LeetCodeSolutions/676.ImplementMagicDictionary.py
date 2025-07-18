"""
LeetCode 676. Implement Magic Dictionary

Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the MagicDictionary class:
- MagicDictionary() Initializes the object.
- void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
- bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any word in the data structure, otherwise returns false.

Example 1:
Input
["MagicDictionary", "buildDict", "search", "search"]
[[], [["hello","leetcode"]], ["hhllo"], ["hello"]]
Output
[null, null, true, false]

Constraints:
- 1 <= dictionary.length <= 100
- 1 <= dictionary[i].length <= 100
- dictionary[i] consists of only lower-case English letters.
- All the strings in dictionary are distinct.
- 1 <= searchWord.length <= 100
- searchWord consists of only lower-case English letters.
- buildDict will be called only once before search.
- At most 100 calls will be made to search.
"""
from typing import List

class MagicDictionary:
    def __init__(self):
        self.words = set()
        self.buckets = {}

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.buckets = {}
        for word in dictionary:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                self.buckets.setdefault(key, set()).add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            key = searchWord[:i] + '*' + searchWord[i+1:]
            words = self.buckets.get(key, set())
            if any(w != searchWord for w in words):
                return True
        return False

# Example usage
if __name__ == "__main__":
    magic = MagicDictionary()
    magic.buildDict(["hello","leetcode"])
    print(magic.search("hhllo"))  # Output: True
    print(magic.search("hello"))  # Output: False

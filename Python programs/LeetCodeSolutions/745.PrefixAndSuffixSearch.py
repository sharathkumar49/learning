"""
LeetCode 745. Prefix and Suffix Search

Design a special dictionary with some words that searchs the words by a prefix and a suffix.

Implement the WordFilter class:
- WordFilter(string[] words) Initializes the object with the words in the dictionary.
- f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix and the suffix. If there is more than one valid index, return the largest. If there is no such word in the dictionary, return -1.

Example 1:
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Constraints:
- 1 <= words.length <= 15000
- 1 <= words[i].length <= 10
- 1 <= prefix.length, suffix.length <= 10
- words[i], prefix and suffix consist of lowercase English letters.
- At most 15000 calls will be made to the function f.
"""
from typing import List

class WordFilter:
    def __init__(self, words: List[str]):
        self.lookup = {}
        for i, word in enumerate(words):
            for p in range(len(word)+1):
                for s in range(len(word)+1):
                    self.lookup[(word[:p], word[s:])] = i
    def f(self, prefix: str, suffix: str) -> int:
        return self.lookup.get((prefix, suffix), -1)

# Example usage
if __name__ == "__main__":
    wf = WordFilter(["apple"])
    print(wf.f("a", "e"))  # Output: 0

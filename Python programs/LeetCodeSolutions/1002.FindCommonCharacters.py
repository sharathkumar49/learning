"""
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.
"""
from typing import List
from collections import Counter

def commonChars(words: List[str]) -> List[str]:
    res = Counter(words[0])
    for word in words[1:]:
        res &= Counter(word)
    return list(res.elements())

# Example usage
if __name__ == "__main__":
    print(commonChars(["bella","label","roller"]))  # Output: ['e', 'l', 'l']
    print(commonChars(["cool","lock","cook"]))      # Output: ['c', 'o']

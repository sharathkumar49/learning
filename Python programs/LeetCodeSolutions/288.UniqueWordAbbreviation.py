"""
288. Unique Word Abbreviation
https://leetcode.com/problems/unique-word-abbreviation/

The abbreviation of a word is the first letter, the number of letters between the first and last letter, and the last letter. Implement the ValidWordAbbr class:
- ValidWordAbbr(dictionary) Initializes the object with the dictionary.
- isUnique(word) Returns true if the abbreviation of word is unique in the dictionary, or false otherwise.

Constraints:
- 1 <= dictionary.length <= 3 * 10^4
- 1 <= dictionary[i].length <= 20
- dictionary[i] consists of lowercase English letters.
- 1 <= word.length <= 20
- word consists of lowercase English letters.

Example:
Input
["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]
[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]
Output
[null,false,true,false,true]
"""
class ValidWordAbbr:
    def __init__(self, dictionary):
        self.abbr = {}
        for word in set(dictionary):
            ab = self._abbr(word)
            if ab not in self.abbr:
                self.abbr[ab] = word
            else:
                if self.abbr[ab] != word:
                    self.abbr[ab] = ''
    def _abbr(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]
    def isUnique(self, word):
        ab = self._abbr(word)
        return ab not in self.abbr or self.abbr[ab] == word

# Example usage:
if __name__ == "__main__":
    vwa = ValidWordAbbr(["deer","door","cake","card"])
    print(vwa.isUnique("dear"))  # Output: False
    print(vwa.isUnique("cart"))  # Output: True
    print(vwa.isUnique("cane"))  # Output: False
    print(vwa.isUnique("make"))  # Output: True

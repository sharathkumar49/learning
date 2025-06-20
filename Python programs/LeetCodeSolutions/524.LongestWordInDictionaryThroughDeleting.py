"""
524. Longest Word in Dictionary through Deleting

Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the one that's smallest lexicographically.

Constraints:
- 1 <= s.length <= 1000
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 1000

Example:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
"""

class Solution:
    def findLongestWord(self, s: str, dictionary: list) -> str:
        def is_subseq(word):
            it = iter(s)
            return all(c in it for c in word)
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            if is_subseq(word):
                return word
        return ""

# Example usage:
sol = Solution()
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
print(sol.findLongestWord(s, dictionary))  # Output: "apple"

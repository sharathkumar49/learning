"""
890. Find and Replace Pattern

Given a list of words and a pattern, return the words that match the pattern.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]

Constraints:
- 1 <= words.length <= 50
- 1 <= pattern.length <= 20
- words[i] and pattern consist of lowercase letters.
"""
def findAndReplacePattern(words, pattern):
    def match(word):
        m1, m2 = {}, {}
        for a, b in zip(word, pattern):
            if m1.setdefault(a, b) != b or m2.setdefault(b, a) != a:
                return False
        return True
    return [w for w in words if match(w)]

# Example usage:
print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))  # Output: ["mee","aqq"]

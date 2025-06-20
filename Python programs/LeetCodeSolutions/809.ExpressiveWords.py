"""
809. Expressive Words

Sometimes people repeat letters to emphasize a word. Given a string s and a list of query words, return the number of words that can be stretched to become s.

Example 1:
Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1

Constraints:
- 1 <= s.length, words.length <= 100
- 1 <= words[i].length <= 100
- s and words[i] consist of lowercase English letters.
"""
def expressiveWords(s, words):
    def check(word):
        i = j = 0
        while i < len(s) and j < len(word):
            if s[i] != word[j]:
                return False
            ch = s[i]
            len1 = len2 = 0
            while i < len(s) and s[i] == ch:
                i += 1
                len1 += 1
            while j < len(word) and word[j] == ch:
                j += 1
                len2 += 1
            if len1 < 3 and len1 != len2:
                return False
            if len1 >= 3 and len2 > len1:
                return False
        return i == len(s) and j == len(word)
    return sum(check(word) for word in words)

# Example usage:
print(expressiveWords("heeellooo", ["hello", "hi", "helo"]))  # Output: 1

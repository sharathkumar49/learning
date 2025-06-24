"""
LeetCode 1408. String Matching in an Array

Given an array of string words, return all strings in words that is a substring of another word in any order.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 30
- words[i] contains only lowercase English letters.

Example:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
"""
def stringMatching(words):
    res = []
    for i, w in enumerate(words):
        for j, ww in enumerate(words):
            if i != j and w in ww:
                res.append(w)
                break
    return res

# Example usage:
words = ["mass","as","hero","superhero"]
print(stringMatching(words))  # Output: ['as', 'hero']

"""
820. Short Encoding of Words

Given a list of words, return the length of the shortest reference string S such that each word can be recovered from S as a suffix.

Example 1:
Input: words = ["time", "me", "bell"]
Output: 10

Constraints:
- 1 <= words.length <= 2000
- 1 <= words[i].length <= 7
- Each word consists of lowercase English letters only.
"""
def minimumLengthEncoding(words):
    words = set(words)
    for w in list(words):
        for k in range(1, len(w)):
            words.discard(w[k:])
    return sum(len(w) + 1 for w in words)

# Example usage:
print(minimumLengthEncoding(["time", "me", "bell"]))  # Output: 10

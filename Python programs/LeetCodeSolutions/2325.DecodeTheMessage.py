"""
LeetCode 2325. Decode the Message

Given key and message, return the decoded message.

Example:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"

Constraints:
- 1 <= key.length <= 100
- 1 <= message.length <= 100
"""

def decodeMessage(key, message):
    d = {}
    idx = 0
    for c in key:
        if c != ' ' and c not in d:
            d[c] = chr(ord('a')+idx)
            idx += 1
    return ''.join(d.get(c, ' ') if c != ' ' else ' ' for c in message)

# Example usage:
# print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))  # Output: "this is a secret"

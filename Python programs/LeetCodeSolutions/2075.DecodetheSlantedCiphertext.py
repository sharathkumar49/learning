"""
LeetCode 2075. Decode the Slanted Ciphertext

Given a string encodedText and an integer rows, decode the slanted ciphertext.

Example:
Input: encodedText = "ch   ie   pr", rows = 3
Output: "cipher"

Constraints:
- 1 <= encodedText.length <= 1000
- 1 <= rows <= 1000
"""

def decodeCiphertext(encodedText, rows):
    n = len(encodedText)
    cols = n // rows
    res = []
    for i in range(cols):
        for j in range(min(rows, cols-i)):
            res.append(encodedText[j*cols + i + j])
    return ''.join(res).rstrip()

# Example usage:
# print(decodeCiphertext("ch   ie   pr", 3))  # Output: "cipher"

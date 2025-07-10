"""
LeetCode 1720. Decode XORed Array

Given the encoded array and the first element, return the original array.

Example 1:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]

Constraints:
- 2 <= n <= 10^4
- 0 <= encoded[i] <= 10^5
- 0 <= first <= 10^5
"""

def decode(encoded, first):
    res = [first]
    for e in encoded:
        res.append(res[-1] ^ e)
    return res

# Example usage:
# encoded = [1,2,3]
# first = 1
# print(decode(encoded, first))  # Output: [1,0,2,1]

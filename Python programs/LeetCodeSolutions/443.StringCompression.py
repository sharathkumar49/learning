"""
443. String Compression

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.
The compressed string should not be returned separately, but instead, be stored in the input character array chars. Return the new length of the array.

Constraints:
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

Example:
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The first 6 characters of the input array should be: ["a","2","b","2","c","3"]
"""

class Solution:
    def compress(self, chars: list) -> int:
        write = 0
        left = 0
        for right in range(len(chars)):
            if right + 1 == len(chars) or chars[right] != chars[right + 1]:
                chars[write] = chars[right]
                write += 1
                cnt = right - left + 1
                if cnt > 1:
                    for c in str(cnt):
                        chars[write] = c
                        write += 1
                left = right + 1
        return write

# Example usage:
sol = Solution()
chars = ["a","a","b","b","c","c","c"]
length = sol.compress(chars)
print(chars[:length])  # Output: ['a', '2', 'b', '2', 'c', '3']

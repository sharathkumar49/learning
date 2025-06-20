"""
434. Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Constraints:
- 0 <= s.length <= 300
- s consists of lower-case and upper-case English letters, digits, or one of the following characters "!@#$%^&*()_+-=',."
- The only space character in s is ' '

Example:
Input: s = "Hello, my name is John"
Output: 5
"""

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

# Example usage:
sol = Solution()
print(sol.countSegments("Hello, my name is John"))  # Output: 5

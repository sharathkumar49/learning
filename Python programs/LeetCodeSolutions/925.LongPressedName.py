"""
925. Long Pressed Name
https://leetcode.com/problems/long-pressed-name/

Your friend is typing their name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
Given two strings name and typed, return true if it is possible that typed was the result of long pressing name.

Constraints:
- 1 <= name.length, typed.length <= 1000
- name and typed consist of only lowercase English letters.

Example:
Input: name = "alex", typed = "aaleex"
Output: true
"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return i == len(name)

# Example usage
if __name__ == "__main__":
    name = "alex"
    typed = "aaleex"
    print(Solution().isLongPressedName(name, typed))  # Output: True

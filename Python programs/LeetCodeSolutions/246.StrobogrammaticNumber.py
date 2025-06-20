"""
246. Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/

Given a string num which represents a number, return true if num is a strobogrammatic number.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Constraints:
- 1 <= num.length <= 50
- num consists of only digits.

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false
"""
def isStrobogrammatic(num):
    pairs = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
    l, r = 0, len(num) - 1
    while l <= r:
        if num[l] not in pairs or pairs[num[l]] != num[r]:
            return False
        l += 1
        r -= 1
    return True

# Example usage:
if __name__ == "__main__":
    print(isStrobogrammatic("69"))   # Output: True
    print(isStrobogrammatic("88"))   # Output: True
    print(isStrobogrammatic("962"))  # Output: False

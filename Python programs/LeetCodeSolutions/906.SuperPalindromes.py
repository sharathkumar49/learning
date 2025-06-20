"""
906. Super Palindromes
https://leetcode.com/problems/super-palindromes/

Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.
Given two positive integers left and right represented as strings, return the number of super-palindromes in the inclusive range [left, right].

Constraints:
- 1 <= left.length, right.length <= 18
- left and right represent integers in the range [1, 10^18].
- left <= right

Example:
Input: left = "4", right = "1000"
Output: 4
"""
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        MAGIC = 100000
        ans = 0
        # odd length
        for k in range(1, MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and str(v) == str(v)[::-1]:
                ans += 1
        # even length
        for k in range(1, MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and str(v) == str(v)[::-1]:
                ans += 1
        return ans

# Example usage
if __name__ == "__main__":
    left = "4"
    right = "1000"
    print(Solution().superpalindromesInRange(left, right))  # Output: 4

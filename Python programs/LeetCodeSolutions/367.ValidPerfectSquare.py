"""
367. Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.

Constraints:
- 1 <= num <= 2^31 - 1
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

# Example usage:
num = 16
print(Solution().isPerfectSquare(num))  # Output: True

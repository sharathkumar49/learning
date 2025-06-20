"""
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible number after removing k digits from num.

Constraints:
- 1 <= k <= num.length <= 10^5
- num consists of only digits.
- num does not have any leading zeros except for the zero itself.
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        final_stack = stack[:-k] if k else stack
        res = ''.join(final_stack).lstrip('0')
        return res if res else '0'

# Example usage:
num = "1432219"
k = 3
print(Solution().removeKdigits(num, k))  # Output: "1219"

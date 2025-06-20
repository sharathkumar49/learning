"""
991. Broken Calculator
https://leetcode.com/problems/broken-calculator/

Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator starting from startValue. The operations are:
- Double the number
- Subtract one

Constraints:
- 1 <= startValue, target <= 10^9

Example:
Input: startValue = 2, target = 3
Output: 2
"""
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target % 2:
                target += 1
            else:
                target //= 2
        return res + startValue - target

# Example usage
if __name__ == "__main__":
    startValue = 2
    target = 3
    print(Solution().brokenCalc(startValue, target))  # Output: 2

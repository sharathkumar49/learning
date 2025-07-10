"""
LeetCode 1742. Maximum Number of Balls in a Box

Given a range of balls numbered from lowLimit to highLimit, return the maximum number of balls in any box, where the box number is the sum of the digits of the ball number.

Example 1:
Input: lowLimit = 1, highLimit = 10
Output: 2

Constraints:
- 1 <= lowLimit <= highLimit <= 10^5
"""

def countBalls(lowLimit, highLimit):
    from collections import Counter
    def digit_sum(x):
        return sum(int(d) for d in str(x))
    cnt = Counter(digit_sum(i) for i in range(lowLimit, highLimit+1))
    return max(cnt.values())

# Example usage:
# lowLimit = 1
# highLimit = 10
# print(countBalls(lowLimit, highLimit))  # Output: 2

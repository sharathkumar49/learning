"""
LeetCode 2480. Maximum Number of Balls in a Box

Given a list of balls, return the maximum number of balls in a box.

Constraints:
- 1 <= lowLimit <= highLimit <= 10^5
"""

def countBalls(lowLimit, highLimit):
    from collections import Counter
    def digit_sum(x):
        return sum(map(int,str(x)))
    cnt = Counter(digit_sum(x) for x in range(lowLimit, highLimit+1))
    return max(cnt.values())

# Example usage:
# print(countBalls(1,10))  # Output: 2

"""
633. Sum of Square Numbers
Difficulty: Medium

Given a non-negative integer c, decide whether it is possible to express c as the sum of two squares.

Example 1:
Input: c = 5
Output: true

Example 2:
Input: c = 3
Output: false

Constraints:
0 <= c <= 2^31 - 1
"""

def judgeSquareSum(c):
    left, right = 0, int(c**0.5)
    while left <= right:
        curr = left*left + right*right
        if curr == c:
            return True
        elif curr < c:
            left += 1
        else:
            right -= 1
    return False

# Example usage
if __name__ == "__main__":
    print(judgeSquareSum(5))  # Output: True
    print(judgeSquareSum(3))  # Output: False

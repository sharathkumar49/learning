"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x. Only the integer part of the square root is returned.

Constraints:
- 0 <= x <= 2^31 - 1

Example:
Input: x = 8
Output: 2

"""
def mySqrt(x: int) -> int:
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Example usage:
if __name__ == "__main__":
    print(mySqrt(8))  # Output: 2
    print(mySqrt(16)) # Output: 4

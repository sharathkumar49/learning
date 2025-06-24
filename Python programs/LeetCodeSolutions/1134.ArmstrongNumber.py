"""
1134. Armstrong Number

Given an integer N, return true if and only if it is an Armstrong number.

Constraints:
- 0 <= N <= 10^8

Example:
Input: N = 153
Output: true
"""
def isArmstrong(N: int) -> bool:
    digits = list(map(int, str(N)))
    k = len(digits)
    return sum(d ** k for d in digits) == N

# Example usage:
N = 153
print(isArmstrong(N))  # Output: True

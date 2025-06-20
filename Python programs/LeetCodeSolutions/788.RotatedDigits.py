"""
788. Rotated Digits

An integer x is called good if after rotating each digit by 180 degrees, we get a valid and different number. Each digit must be rotated: 0, 1, and 8 stay the same; 2 <-> 5, 6 <-> 9; 3, 4, and 7 are invalid. Given n, return the number of good integers in the range [1, n].

Example 1:
Input: n = 10
Output: 4

Example 2:
Input: n = 1
Output: 0

Constraints:
- 1 <= n <= 10^4
"""
def rotatedDigits(n):
    count = 0
    for i in range(1, n+1):
        s = str(i)
        if any(c in s for c in '347'):
            continue
        if any(c in s for c in '2569'):
            count += 1
    return count

# Example usage:
print(rotatedDigits(10))  # Output: 4
print(rotatedDigits(1))   # Output: 0

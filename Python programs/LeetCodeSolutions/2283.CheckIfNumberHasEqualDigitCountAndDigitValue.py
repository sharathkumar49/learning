"""
LeetCode 2283. Check if Number Has Equal Digit Count and Digit Value

Given num, return true if each digit has the same count as its value.

Example:
Input: num = "1210"
Output: True

Constraints:
- 1 <= num.length <= 10
"""

def digitCount(num):
    from collections import Counter
    c = Counter(num)
    return all(c[str(i)] == int(num[i]) for i in range(len(num)))

# Example usage:
# print(digitCount("1210"))  # Output: True

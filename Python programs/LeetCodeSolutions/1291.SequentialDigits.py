"""
LeetCode 1291. Sequential Digits

Return a sorted list of all the integers in the range [low, high] that have sequential digits.

Constraints:
- 10 <= low <= high <= 10^9

Example:
Input: low = 100, high = 300
Output: [123,234]
"""
def sequentialDigits(low, high):
    res = []
    s = '123456789'
    for l in range(2, 10):
        for i in range(10 - l + 1):
            num = int(s[i:i+l])
            if low <= num <= high:
                res.append(num)
    return res

# Example usage:
low = 100
high = 300
print(sequentialDigits(low, high))  # Output: [123, 234]

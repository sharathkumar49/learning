"""
LeetCode 2165. Smallest Value of the Rearranged Number

Given an integer num, rearrange its digits to get the smallest possible value (if num is negative, the largest possible value). Return the result as an integer.

Example:
Input: num = 310
Output: 103

Constraints:
- -10^9 <= num <= 10^9
"""

def smallestNumber(num):
    if num == 0:
        return 0
    s = list(str(abs(num)))
    if num > 0:
        s.sort()
        if s[0] == '0':
            for i in range(1, len(s)):
                if s[i] != '0':
                    s[0], s[i] = s[i], s[0]
                    break
        return int(''.join(s))
    else:
        s.sort(reverse=True)
        return -int(''.join(s))

# Example usage:
# print(smallestNumber(310))  # Output: 103

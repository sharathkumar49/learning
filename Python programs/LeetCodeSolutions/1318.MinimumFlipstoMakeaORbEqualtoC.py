"""
LeetCode 1318. Minimum Flips to Make a OR b Equal to c

Given 3 integers a, b, c, return the minimum number of flips required in the binary representations of a and b so that (a OR b == c).

Constraints:
- 1 <= a, b, c <= 10^9

Example:
Input: a = 2, b = 6, c = 5
Output: 3
"""
def minFlips(a, b, c):
    res = 0
    for i in range(32):
        abit = (a >> i) & 1
        bbit = (b >> i) & 1
        cbit = (c >> i) & 1
        if cbit == 0:
            res += abit + bbit
        else:
            res += (abit | bbit) ^ 1
    return res

# Example usage:
a = 2
b = 6
c = 5
print(minFlips(a, b, c))  # Output: 3

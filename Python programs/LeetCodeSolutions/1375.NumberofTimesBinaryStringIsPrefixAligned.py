"""
LeetCode 1375. Number of Times Binary String Is Prefix-Aligned

Given a permutation of [1,2,...,n] as flips, return the number of times the binary string is prefix-aligned after each flip.

Constraints:
- 1 <= n <= 5 * 10^4
- flips is a permutation of [1,2,...,n]

Example:
Input: flips = [3,2,4,1,5]
Output: 2
"""
def numTimesAllBlue(flips):
    res = 0
    right = 0
    for i, f in enumerate(flips):
        right = max(right, f)
        if right == i+1:
            res += 1
    return res

# Example usage:
flips = [3,2,4,1,5]
print(numTimesAllBlue(flips))  # Output: 2

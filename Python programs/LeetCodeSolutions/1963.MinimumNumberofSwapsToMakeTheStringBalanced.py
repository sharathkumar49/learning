"""
LeetCode 1963. Minimum Number of Swaps to Make the String Balanced

Given a string s of brackets, return the minimum number of swaps to make the string balanced.

Example:
Input: s = "][]["
Output: 1

Constraints:
- 1 <= s.length <= 10^5
- s consists of '[' and ']'.
- s.length is even
"""

def minSwaps(s):
    max_unbalanced = curr = 0
    for c in s:
        if c == '[':
            curr -= 1
        else:
            curr += 1
        max_unbalanced = max(max_unbalanced, curr)
    return (max_unbalanced + 1) // 2

# Example usage:
# print(minSwaps("][]["))  # Output: 1

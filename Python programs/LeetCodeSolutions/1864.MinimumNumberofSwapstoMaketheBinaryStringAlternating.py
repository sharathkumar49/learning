"""
LeetCode 1864. Minimum Number of Swaps to Make the Binary String Alternating

Given a binary string s, return the minimum number of swaps to make s alternating, or -1 if impossible.

Example:
Input: s = "111000"
Output: 1

Constraints:
- 1 <= s.length <= 1000
- s[i] is either '0' or '1'.
"""

def minSwaps(s):
    n = len(s)
    ones = s.count('1')
    zeros = n - ones
    if abs(ones - zeros) > 1:
        return -1
    def count_swaps(start):
        swaps = 0
        for i, c in enumerate(s):
            if int(c) != (i + start) % 2:
                swaps += 1
        return swaps // 2
    if ones > zeros:
        return count_swaps(1)
    elif zeros > ones:
        return count_swaps(0)
    else:
        return min(count_swaps(0), count_swaps(1))

# Example usage:
print(minSwaps("111000"))  # Output: 1

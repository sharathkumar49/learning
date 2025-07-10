"""
LeetCode 1933. Minimum Moves to Make String Equal

Given a string s, return the minimum number of moves to make all characters equal. In one move, you can increment or decrement a character.

Example:
Input: s = "abc"
Output: 2

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

def minMoves(s):
    arr = sorted(ord(c) for c in s)
    median = arr[len(arr)//2]
    return sum(abs(x - median) for x in arr)

# Example usage:
# print(minMoves("abc"))  # Output: 2

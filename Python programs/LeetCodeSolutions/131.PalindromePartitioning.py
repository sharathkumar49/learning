"""
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Constraints:
- 1 <= s.length <= 16
- s consists of only lowercase English letters.

Example:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""
from typing import List

def partition(s: str) -> List[List[str]]:
    res = []
    def is_palindrome(sub):
        return sub == sub[::-1]
    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start+1, len(s)+1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])
    backtrack(0, [])
    return res

# Example usage:
if __name__ == "__main__":
    print(partition("aab"))  # Output: [["a","a","b"],["aa","b"]]

"""
899. Orderly Queue
https://leetcode.com/problems/orderly-queue/

You are given a string s and an integer k. You can choose one of the first k letters of s and move it to the end of the string.
Return the lexicographically smallest string you could have after applying the mentioned move any number of times.

Constraints:
- 1 <= k <= s.length <= 1000
- s consists of lowercase English letters.

Example:
Input: s = "cba", k = 1
Output: "acb"
"""
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))

# Example usage
if __name__ == "__main__":
    s = "cba"
    k = 1
    print(Solution().orderlyQueue(s, k))  # Output: "acb"

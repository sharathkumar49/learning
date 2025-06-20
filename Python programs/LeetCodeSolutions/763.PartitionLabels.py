"""
LeetCode 763. Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Constraints:
- 1 <= S.length <= 500
- S consists of lowercase English letters.
"""
from typing import List

def partitionLabels(S: str) -> List[int]:
    last = {c: i for i, c in enumerate(S)}
    res = []
    start = end = 0
    for i, c in enumerate(S):
        end = max(end, last[c])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res

# Example usage
if __name__ == "__main__":
    print(partitionLabels("ababcbacadefegdehijhklij"))  # Output: [9,7,8]

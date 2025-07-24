"""
LeetCode 2522. Partition String Into Substrings With Values at Most K

Given a string s and integer k, partition s into the minimum number of substrings with values at most k.

Constraints:
- 1 <= s.length <= 10^5
- 1 <= k <= 10^9
"""

def minimumPartition(s, k):
    cnt = 0
    i = 0
    n = len(s)
    while i < n:
        j = i
        while j < n and int(s[i:j+1]) <= k:
            j += 1
        if i == j:
            return -1
        cnt += 1
        i = j
    return cnt
# Example usage:
# print(minimumPartition("165462", 60))  # Output: 4

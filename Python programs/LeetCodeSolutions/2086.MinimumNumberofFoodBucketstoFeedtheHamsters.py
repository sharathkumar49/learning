"""
LeetCode 2086. Minimum Number of Food Buckets to Feed the Hamsters

Given a string hamsters, return the minimum number of buckets needed to feed all hamsters, or -1 if impossible.

Example:
Input: hamsters = "H..H"
Output: 2

Constraints:
- 1 <= hamsters.length <= 10^5
- hamsters consists only of 'H' and '.'
"""

def minimumBuckets(hamsters):
    n = len(hamsters)
    hamsters = list(hamsters)
    res = 0
    for i in range(n):
        if hamsters[i] == 'H':
            if i > 0 and hamsters[i-1] == 'B':
                continue
            if i+1 < n and hamsters[i+1] == '.':
                hamsters[i+1] = 'B'
                res += 1
            elif i > 0 and hamsters[i-1] == '.':
                hamsters[i-1] = 'B'
                res += 1
            else:
                return -1
    return res

# Example usage:
print(minimumBuckets("H..H"))  # Output: 2

"""
LeetCode 2168. Unique Substrings With Equal Digit Frequency

Given a string s, return the number of unique non-empty substrings where each digit appears the same number of times.

Example:
Input: s = "1212"
Output: 5

Constraints:
- 1 <= s.length <= 100
- s consists of digits '0'-'9'.
"""

def equalDigitFrequency(s):
    res = set()
    n = len(s)
    for i in range(n):
        cnt = [0]*10
        for j in range(i, n):
            cnt[int(s[j])] += 1
            if len(set([x for x in cnt if x>0])) == 1:
                res.add(s[i:j+1])
    return len(res)

# Example usage:
# print(equalDigitFrequency("1212"))  # Output: 5

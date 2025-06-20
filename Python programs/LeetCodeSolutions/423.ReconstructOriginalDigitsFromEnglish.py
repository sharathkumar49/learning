"""
423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
"""
class Solution:
    def originalDigits(self, s: str) -> str:
        from collections import Counter
        count = Counter(s)
        out = {}
        out['0'] = count['z']
        out['2'] = count['w']
        out['4'] = count['u']
        out['6'] = count['x']
        out['8'] = count['g']
        out['3'] = count['h'] - out['8']
        out['5'] = count['f'] - out['4']
        out['7'] = count['s'] - out['6']
        out['1'] = count['o'] - out['0'] - out['2'] - out['4']
        out['9'] = count['i'] - out['5'] - out['6'] - out['8']
        res = ''.join([k * out[k] for k in sorted(out.keys())])
        return res

# Example usage:
s = "owoztneoer"
print(Solution().originalDigits(s))  # Output: "012"

"""
1234. Replace the Substring for Balanced String

Given a string s, return the minimum length of a substring that can be replaced to make s balanced. A string is balanced if each of 'Q', 'W', 'E', 'R' appears n/4 times.

Constraints:
- 4 <= s.length <= 10^5
- s.length is a multiple of 4
- s consists of 'Q', 'W', 'E', 'R'.

Example:
Input: s = "QWER"
Output: 0

"""
def balancedString(s):
    from collections import Counter
    n = len(s)
    count = Counter(s)
    res = n
    left = 0
    for right in range(n):
        count[s[right]] -= 1
        while left < n and all(count[c] <= n//4 for c in 'QWER'):
            res = min(res, right - left + 1)
            count[s[left]] += 1
            left += 1
    return res

# Example usage
if __name__ == "__main__":
    print(balancedString("QWER"))  # Output: 0

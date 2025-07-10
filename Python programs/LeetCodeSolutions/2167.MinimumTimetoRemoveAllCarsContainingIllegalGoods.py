"""
LeetCode 2167. Minimum Time to Remove All Cars Containing Illegal Goods

Given a binary string s, where '1' means a car contains illegal goods, return the minimum time to remove all such cars. You can remove a car from the left or right in 1 unit of time, or remove any car with illegal goods in 2 units of time.

Example:
Input: s = "1100101"
Output: 5

Constraints:
- 1 <= s.length <= 10^5
- s[i] is '0' or '1'.
"""

def minimumTime(s):
    n = len(s)
    left = [0]*n
    right = [0]*n
    left[0] = 2 if s[0]=='1' else 0
    for i in range(1, n):
        left[i] = min(left[i-1]+1, (i+1)*2) if s[i]=='1' else left[i-1]
    right[-1] = 2 if s[-1]=='1' else 0
    for i in range(n-2, -1, -1):
        right[i] = min(right[i+1]+1, (n-i)*2) if s[i]=='1' else right[i+1]
    res = min(left[-1], right[0])
    for i in range(n-1):
        res = min(res, left[i]+right[i+1])
    return res

# Example usage:
# print(minimumTime("1100101"))  # Output: 5

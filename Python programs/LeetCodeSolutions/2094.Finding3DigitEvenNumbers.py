"""
LeetCode 2094. Finding 3-Digit Even Numbers

Given an array of digits, return all unique 3-digit even numbers that can be formed.

Example:
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]

Constraints:
- 3 <= digits.length <= 100
- 0 <= digits[i] <= 9
"""

def findEvenNumbers(digits):
    from collections import Counter
    res = set()
    cnt = Counter(digits)
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10, 2):
                c = Counter([i, j, k])
                if all(cnt[d] >= c[d] for d in c):
                    res.add(i*100 + j*10 + k)
    return sorted(res)

# Example usage:
# print(findEvenNumbers([2,1,3,0]))  # Output: [102,120,130,132,210,230,302,310,312,320]

"""
LeetCode 2217. Find Palindrome With Fixed Length

Given queries and intLength, return the k-th smallest palindrome of intLength for each query.

Example:
Input: queries = [1,2,3], intLength = 3
Output: [101,111,121]

Constraints:
- 1 <= queries.length <= 5 * 10^4
- 1 <= queries[i] <= 10^9
- 1 <= intLength <= 15
"""

def kthPalindrome(queries, intLength):
    res = []
    half = (intLength+1)//2
    start = 10**(half-1)
    for k in queries:
        num = start + k - 1
        s = str(num)
        pal = s + s[:-1][::-1] if intLength%2 else s + s[::-1]
        if len(pal) == intLength:
            res.append(int(pal))
        else:
            res.append(-1)
    return res

# Example usage:
# print(kthPalindrome([1,2,3], 3))  # Output: [101,111,121]

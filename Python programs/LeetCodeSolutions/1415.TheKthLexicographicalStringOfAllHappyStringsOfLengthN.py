"""
LeetCode 1415. The k-th Lexicographical String of All Happy Strings of Length n

A happy string is a string that consists only of 'a', 'b', and 'c', and no two adjacent characters are the same. Given two integers n and k, return the k-th lexicographical happy string of length n or an empty string if there are less than k happy strings of length n.

Constraints:
- 1 <= n <= 10
- 1 <= k <= 100

Example:
Input: n = 3, k = 9
Output: "cab"
"""
def getHappyString(n, k):
    from itertools import product
    res = []
    def is_happy(s):
        return all(s[i] != s[i+1] for i in range(len(s)-1))
    for p in product('abc', repeat=n):
        s = ''.join(p)
        if is_happy(s):
            res.append(s)
    res.sort()
    return res[k-1] if k <= len(res) else ""

# Example usage:
n = 3
k = 9
print(getHappyString(n, k))  # Output: "cab"

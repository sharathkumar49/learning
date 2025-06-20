"""
247. Strobogrammatic Number II
https://leetcode.com/problems/strobogrammatic-number-ii/

Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

Constraints:
- 1 <= n <= 14

Example 1:
Input: n = 2
Output: ["11","69","88","96"]

Example 2:
Input: n = 1
Output: ["0","1","8"]
"""
def findStrobogrammatic(n):
    def helper(n, final_n):
        if n == 0: return ['']
        if n == 1: return ['0','1','8']
        prev = helper(n-2, final_n)
        res = []
        for s in prev:
            for a, b in [('0','0'),('1','1'),('6','9'),('8','8'),('9','6')]:
                if n != final_n or a != '0':
                    res.append(a + s + b)
        return res
    return helper(n, n)

# Example usage:
if __name__ == "__main__":
    print(findStrobogrammatic(2))  # Output: ["11","69","88","96"]
    print(findStrobogrammatic(1))  # Output: ["0","1","8"]

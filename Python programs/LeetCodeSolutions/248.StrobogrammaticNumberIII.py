"""
248. Strobogrammatic Number III
https://leetcode.com/problems/strobogrammatic-number-iii/

Given two strings low and high that represent two integers, return the count of strobogrammatic numbers in the range [low, high], inclusive.

Constraints:
- 1 <= low.length, high.length <= 15
- 0 <= int(low) <= int(high) <= 10^15
- low and high do not contain any leading zeros except for "0" itself.

Example 1:
Input: low = "50", high = "100"
Output: 3

Example 2:
Input: low = "0", high = "0"
Output: 1
"""
def strobogrammaticInRange(low, high):
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
    res = 0
    for length in range(len(low), len(high)+1):
        for num in helper(length, length):
            if (len(num) == 1 or num[0] != '0') and (len(num) > 1 or num == '0'):
                if int(low) <= int(num) <= int(high):
                    res += 1
    return res

# Example usage:
if __name__ == "__main__":
    print(strobogrammaticInRange("50", "100"))  # Output: 3
    print(strobogrammaticInRange("0", "0"))     # Output: 1

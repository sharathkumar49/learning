"""
984. String Without AAA or BBB
https://leetcode.com/problems/string-without-aaa-or-bbb/

Given two integers a and b, return any string s such that:
- s has length a + b
- s contains exactly a 'a' letters, and exactly b 'b' letters
- The substring 'aaa' does not occur in s
- The substring 'bbb' does not occur in s

Constraints:
- 0 <= a, b <= 100
- It is guaranteed such a string exists for the given a and b.

Example:
Input: a = 1, b = 2
Output: "abb"
"""
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if (a > b and (len(res) < 2 or not (res[-1] == res[-2] == 'a'))):
                res.append('a')
                a -= 1
            elif (b > a and (len(res) < 2 or not (res[-1] == res[-2] == 'b'))):
                res.append('b')
                b -= 1
            else:
                if len(res) >= 2 and res[-1] == res[-2]:
                    if res[-1] == 'a':
                        res.append('b')
                        b -= 1
                    else:
                        res.append('a')
                        a -= 1
                elif a > 0:
                    res.append('a')
                    a -= 1
                else:
                    res.append('b')
                    b -= 1
        return ''.join(res)

# Example usage
if __name__ == "__main__":
    a = 1
    b = 2
    print(Solution().strWithout3a3b(a, b))  # Output: "abb"

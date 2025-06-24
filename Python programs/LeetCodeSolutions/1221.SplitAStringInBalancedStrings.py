"""
1221. Split a String in Balanced Strings

Given a string s, return the maximum number of balanced strings you can split it into. A balanced string has equal number of 'L' and 'R'.

Constraints:
- 1 <= s.length <= 1000
- s[i] is 'L' or 'R'.

Example:
Input: s = "RLRRLLRLRL"
Output: 4

"""
def balancedStringSplit(s):
    res = 0
    bal = 0
    for c in s:
        bal += 1 if c == 'R' else -1
        if bal == 0:
            res += 1
    return res

# Example usage
if __name__ == "__main__":
    print(balancedStringSplit("RLRRLLRLRL"))  # Output: 4

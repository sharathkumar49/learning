"""
816. Ambiguous Coordinates

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)", and we removed all commas, decimal points, and spaces, and wrote them as a string s. Return a list of all possible original coordinate representations.

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(1, 2.3)", "(12, 3)", "(1.2, 3)"]

Constraints:
- 4 <= s.length <= 12
- s[0] == '('
- s[s.length - 1] == ')'
- The rest of s are digits.
"""
def ambiguousCoordinates(s):
    def make(s):
        res = []
        if s == "0" or not s.startswith("0"):
            res.append(s)
        for i in range(1, len(s)):
            left, right = s[:i], s[i:]
            if (left == "0" or not left.startswith("0")) and not right.endswith("0"):
                res.append(left + "." + right)
        return res
    s = s[1:-1]
    ans = []
    for i in range(1, len(s)):
        for a in make(s[:i]):
            for b in make(s[i:]):
                ans.append(f"({a}, {b})")
    return ans

# Example usage:
print(ambiguousCoordinates("(123)"))  # Output: ["(1, 23)", "(1, 2.3)", "(12, 3)", "(1.2, 3)"]

"""
784. Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:
- 1 <= s.length <= 12
- s consists of letters and digits.
"""
def letterCasePermutation(s):
    res = ['']
    for c in s:
        if c.isalpha():
            res = [i + j for i in res for j in [c.lower(), c.upper()]]
        else:
            res = [i + c for i in res]
    return res

# Example usage:
print(letterCasePermutation("a1b2"))  # Output: ["a1b2","a1B2","A1b2","A1B2"]
print(letterCasePermutation("3z4"))   # Output: ["3z4","3Z4"]

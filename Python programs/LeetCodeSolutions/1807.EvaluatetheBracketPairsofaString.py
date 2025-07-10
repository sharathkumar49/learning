"""
LeetCode 1807. Evaluate the Bracket Pairs of a String

Given a string s and a list of knowledge (pairs of key and value), replace all bracketed keys in s with their corresponding values.

Example 1:
Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"

Constraints:
- 1 <= s.length <= 10^5
- 1 <= knowledge.length <= 10^5
- knowledge[i].length == 2
- 1 <= knowledge[i][0], knowledge[i][1] <= 10
- s consists of lowercase English letters and round brackets
"""

def evaluate(s, knowledge):
    d = dict(knowledge)
    res = []
    i = 0
    while i < len(s):
        if s[i] == '(': 
            j = i+1
            while s[j] != ')':
                j += 1
            key = s[i+1:j]
            res.append(d.get(key, '?'))
            i = j+1
        else:
            res.append(s[i])
            i += 1
    return ''.join(res)

# Example usage:
# s = "(name)is(age)yearsold"
# knowledge = [["name","bob"],["age","two"]]
# print(evaluate(s, knowledge))  # Output: "bobistwoyearsold"

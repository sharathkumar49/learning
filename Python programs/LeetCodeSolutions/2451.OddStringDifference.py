"""
LeetCode 2451. Odd String Difference

Given a list of words, return the odd string out based on character differences.

Constraints:
- 3 <= words.length <= 100
- 2 <= words[i].length <= 100
"""

def oddString(words):
    diffs = [ [ord(b)-ord(a) for a,b in zip(w,w[1:])] for w in words ]
    for d in diffs:
        if diffs.count(d) == 1:
            return words[diffs.index(d)]

# Example usage:
# print(oddString(["adc","wzy","abc"]))  # Output: "abc"

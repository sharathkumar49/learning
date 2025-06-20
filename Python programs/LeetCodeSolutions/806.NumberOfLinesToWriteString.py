"""
806. Number of Lines To Write String

You are given a list widths of length 26, where widths[i] is the width of the i-th lowercase letter. Given a string s, write it on lines such that each line has a maximum width of 100. Return the number of lines and the width of the last line.

Example 1:
Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]

Example 2:
Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
Output: [2, 4]

Constraints:
- widths.length == 26
- 2 <= s.length <= 1000
- s contains only lowercase English letters.
"""
def numberOfLines(widths, s):
    lines = 1
    width = 0
    for c in s:
        w = widths[ord(c) - ord('a')]
        if width + w > 100:
            lines += 1
            width = w
        else:
            width += w
    return [lines, width]

# Example usage:
print(numberOfLines([10]*26, "abcdefghijklmnopqrstuvwxyz"))  # Output: [3, 60]
print(numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))  # Output: [2, 4]

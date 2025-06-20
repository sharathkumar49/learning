"""
1055. Shortest Way to Form String

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If impossible, return -1.

Constraints:
- 1 <= source.length, target.length <= 1000
- source and target consist of lowercase English letters.

Example:
Input: source = "abc", target = "abcbc"
Output: 2
"""
def shortestWay(source: str, target: str) -> int:
    res = i = 0
    while i < len(target):
        j = 0
        k = i
        while j < len(source) and i < len(target):
            if source[j] == target[i]:
                i += 1
            j += 1
        if k == i:
            return -1
        res += 1
    return res

# Example usage:
source = "abc"
target = "abcbc"
print(shortestWay(source, target))  # Output: 2

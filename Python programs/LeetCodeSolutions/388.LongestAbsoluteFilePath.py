"""
388. Longest Absolute File Path

Given a string input representing the file system in a file, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Constraints:
- 1 <= input.length <= 10^4
- input may contain lowercase or uppercase English letters, a new line character '\n', a tab character '\t', a dot '.', and a space ' '.
"""
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {0: 0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen

# Example usage:
input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(Solution().lengthLongestPath(input))  # Output: 20

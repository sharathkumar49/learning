"""
71. Simplify Path
https://leetcode.com/problems/simplify-path/

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

Constraints:
- 1 <= path.length <= 3000
- path consists of English letters, digits, '.', '/', or '_'.

Example:
Input: path = "/home/"
Output: "/home"

"""
def simplifyPath(path: str) -> str:
    stack = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)

# Example usage:
if __name__ == "__main__":
    print(simplifyPath("/home/"))  # Output: "/home"
    print(simplifyPath("/a/./b/../../c/"))  # Output: "/c"

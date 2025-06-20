"""
LeetCode 722. Remove Comments

Given a C++ program, remove comments from it. The program source code is an array of strings source where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character '\n'.

In C++, there are two types of comments:
1. Line comments start with // and continue to the end of the line.
2. Block comments start with /* and end with */. They can be multi-line.

Return the source code after removing the comments. You will return the answer as a list of strings.

Example 1:
Input: source = ["/*Test program */", "int main()", "// start", " code", "int a = 1;", "int b = 2;", "return 0;"]
Output: ["int main()", " code", "int a = 1;", "int b = 2;", "return 0;"]

Constraints:
- 1 <= source.length <= 100
- 0 <= source[i].length <= 80
- source[i] consists of printable ASCII characters.
"""
from typing import List

def removeComments(source: List[str]) -> List[str]:
    res = []
    in_block = False
    buf = ''
    for line in source:
        i = 0
        while i < len(line):
            if not in_block and i+1 < len(line) and line[i:i+2] == '/*':
                in_block = True
                i += 2
            elif in_block and i+1 < len(line) and line[i:i+2] == '*/':
                in_block = False
                i += 2
            elif not in_block and i+1 < len(line) and line[i:i+2] == '//':
                break
            elif not in_block:
                buf += line[i]
                i += 1
            else:
                i += 1
        if not in_block and buf:
            res.append(buf)
            buf = ''
    return res

# Example usage
if __name__ == "__main__":
    source = ["/*Test program */", "int main()", "// start", " code", "int a = 1;", "int b = 2;", "return 0;"]
    print(removeComments(source))

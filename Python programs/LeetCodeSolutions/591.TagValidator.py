"""
591. Tag Validator
Difficulty: Hard

Given a string representing a code snippet, return true if it is a valid code and false otherwise. A code snippet is valid if all the following rules are satisfied:
- The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
- A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same.
- A valid tag name consists of only upper-case letters, and has length in the range [1,9].
- A tag can contain another tag. However, the content between two tags cannot be another tag.
- CDATA is allowed as content. The format is <![CDATA[CDATA_CONTENT]]>, where CDATA_CONTENT can be any characters. The function of CDATA is to forbid the validator to parse CDATA_CONTENT.
- Tags cannot be partially closed.

Example 1:
Input: code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
Output: true

Example 2:
Input: code = "<A>  <B> </A>   </B>"
Output: false

Constraints:
1 <= code.length <= 50000
code consists of English letters, digits, '<', '>', '/', '!', '[', ']', '=', ' ', and other printable characters.
"""

def isValid(code: str) -> bool:
    stack = []
    i = 0
    n = len(code)
    while i < n:
        if code.startswith('<![CDATA[', i):
            j = code.find(']]>', i)
            if j == -1:
                return False
            i = j + 3
        elif code.startswith('</', i):
            j = code.find('>', i)
            if j == -1:
                return False
            tag = code[i+2:j]
            if not stack or stack[-1] != tag:
                return False
            stack.pop()
            i = j + 1
            if not stack and i != n:
                return False
        elif code.startswith('<', i):
            j = code.find('>', i)
            if j == -1:
                return False
            tag = code[i+1:j]
            if not (1 <= len(tag) <= 9 and tag.isupper()):
                return False
            stack.append(tag)
            i = j + 1
        else:
            if not stack:
                return False
            i += 1
    return not stack

# Example usage
if __name__ == "__main__":
    print(isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))  # Output: True
    print(isValid("<A>  <B> </A>   </B>"))  # Output: False

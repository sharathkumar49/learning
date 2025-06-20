"""
65. Valid Number
https://leetcode.com/problems/valid-number/

A valid number can be split up into these components (in order):
- A decimal number or an integer.
- (Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- One of the following formats:
    - At least one digit, followed by a dot '.'
    - At least one digit, followed by a dot '.', followed by at least one digit
    - A dot '.', followed by at least one digit
An integer can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- At least one digit

Constraints:
- 1 <= s.length <= 20
- s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'

Example:
Input: s = "0"
Output: true

"""
def isNumber(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    try:
        float(s)
        # Reject cases like '1e', 'e9', '--6', etc.
        if s.lower().count('e') > 1:
            return False
        if s.count('.') > 1:
            return False
        if any(c.isalpha() and c.lower() != 'e' for c in s):
            return False
        return True
    except ValueError:
        return False

# Example usage:
if __name__ == "__main__":
    print(isNumber("0"))        # Output: True
    print(isNumber("e"))        # Output: False
    print(isNumber(".1"))      # Output: True
    print(isNumber("1e10"))    # Output: True
    print(isNumber("1e"))      # Output: False

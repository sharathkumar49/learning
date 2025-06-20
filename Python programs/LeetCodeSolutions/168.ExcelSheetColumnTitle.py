"""
168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

Constraints:
- 1 <= columnNumber <= 2^31 - 1

Example:
Input: columnNumber = 28
Output: "AB"
"""
def convertToTitle(columnNumber: int) -> str:
    res = []
    while columnNumber:
        columnNumber -= 1
        res.append(chr(columnNumber % 26 + ord('A')))
        columnNumber //= 26
    return ''.join(reversed(res))

# Example usage:
if __name__ == "__main__":
    print(convertToTitle(1))   # Output: "A"
    print(convertToTitle(28))  # Output: "AB"
    print(convertToTitle(701)) # Output: "ZY"

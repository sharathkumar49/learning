"""
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

Constraints:
- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.

Example:
Input: columnTitle = "AB"
Output: 28
"""
def titleToNumber(columnTitle: str) -> int:
    res = 0
    for c in columnTitle:
        res = res * 26 + (ord(c) - ord('A') + 1)
    return res

# Example usage:
if __name__ == "__main__":
    print(titleToNumber("A"))   # Output: 1
    print(titleToNumber("AB"))  # Output: 28
    print(titleToNumber("ZY"))  # Output: 701

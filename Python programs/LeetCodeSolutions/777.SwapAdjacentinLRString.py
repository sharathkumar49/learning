"""
777. Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X', you can swap adjacent 'X' and 'L' ("XL" -> "LX") or 'R' and 'X' ("RX" -> "XR"). Given two strings start and end, return true if and only if end can be reached from start by performing these moves any number of times.

Example 1:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true

Example 2:
Input: start = "X", end = "L"
Output: false

Constraints:
- 1 <= start.length == end.length <= 10^4
- Both start and end only contain 'L', 'R', and 'X'.
"""
def canTransform(start, end):
    if start.replace('X', '') != end.replace('X', ''):
        return False
    i = j = 0
    n = len(start)
    while i < n and j < n:
        while i < n and start[i] == 'X': i += 1
        while j < n and end[j] == 'X': j += 1
        if i == n and j == n:
            return True
        if i == n or j == n:
            return False
        if start[i] != end[j]:
            return False
        if start[i] == 'L' and i < j:
            return False
        if start[i] == 'R' and i > j:
            return False
        i += 1
        j += 1
    return True

# Example usage:
print(canTransform("RXXLRXRXL", "XRLXXRRLX"))  # Output: True
print(canTransform("X", "L"))  # Output: False

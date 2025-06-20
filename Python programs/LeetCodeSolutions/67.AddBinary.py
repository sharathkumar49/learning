"""
67. Add Binary
https://leetcode.com/problems/add-binary/

Given two binary strings a and b, return their sum as a binary string.

Constraints:
- 1 <= a.length, b.length <= 10^4
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

Example:
Input: a = "11", b = "1"
Output: "100"

"""
def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        res.append(str(total % 2))
        carry = total // 2
    return ''.join(reversed(res))

# Example usage:
if __name__ == "__main__":
    print(addBinary("11", "1"))  # Output: "100"
    print(addBinary("1010", "1011"))  # Output: "10101"

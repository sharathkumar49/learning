"""
165. Compare Version Numbers
https://leetcode.com/problems/compare-version-numbers/

Given two version numbers, version1 and version2, compare them.

Constraints:
- 1 <= version1.length, version2.length <= 500
- version1 and version2 only contain digits and '.'

Example:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
"""
def compareVersion(version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    n, m = len(v1), len(v2)
    for i in range(max(n, m)):
        num1 = v1[i] if i < n else 0
        num2 = v2[i] if i < m else 0
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
    return 0

# Example usage:
if __name__ == "__main__":
    print(compareVersion("1.01", "1.001"))  # Output: 0
    print(compareVersion("1.0", "1.0.0"))   # Output: 0
    print(compareVersion("0.1", "1.1"))     # Output: -1

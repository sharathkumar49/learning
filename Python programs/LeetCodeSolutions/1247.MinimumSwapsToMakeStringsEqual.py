"""
1247. Minimum Swaps to Make Strings Equal

Given two strings s1 and s2 of equal length, return the minimum number of swaps to make the strings equal. Only swaps of 'x' and 'y' are allowed.

Constraints:
- 1 <= s1.length, s2.length <= 1000
- s1 and s2 consist of 'x' and 'y'.

Example:
Input: s1 = "xx", s2 = "yy"
Output: 1

"""
def minimumSwap(s1, s2):
    xy = yx = 0
    for a, b in zip(s1, s2):
        if a == 'x' and b == 'y':
            xy += 1
        elif a == 'y' and b == 'x':
            yx += 1
    if (xy + yx) % 2:
        return -1
    return xy // 2 + yx // 2 + 2 * (xy % 2)

# Example usage
if __name__ == "__main__":
    print(minimumSwap("xx", "yy"))  # Output: 1

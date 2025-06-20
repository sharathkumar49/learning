"""
791. Custom Sort String

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously. Permute the characters of s so that they match the order that order was sorted. Characters not in order can be placed anywhere.

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"

Example 2:
Input: order = "bcafg", s = "abcd"
Output: "bcad"

Constraints:
- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters.
- All the characters of order are unique.
"""
def customSortString(order, s):
    order_map = {c: i for i, c in enumerate(order)}
    return ''.join(sorted(s, key=lambda c: order_map.get(c, 26)))

# Example usage:
print(customSortString("cba", "abcd"))  # Output: "cbad"
print(customSortString("bcafg", "abcd"))  # Output: "bcad"

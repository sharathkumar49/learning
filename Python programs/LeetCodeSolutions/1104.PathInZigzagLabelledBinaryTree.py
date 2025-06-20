"""
1104. Path In Zigzag Labelled Binary Tree

In a binary tree with zigzag labelling, return the path from the root to the given label.

Constraints:
- 1 <= label <= 10^6

Example:
Input: label = 14
Output: [1,3,4,14]
"""
def pathInZigZagTree(label: int) -> list:
    res = []
    while label:
        res.append(label)
        level = label.bit_length() - 1
        label = (3 << level) - 1 - label // 2
    return res[::-1]

# Example usage:
label = 14
print(pathInZigZagTree(label))  # Output: [1, 3, 4, 14]

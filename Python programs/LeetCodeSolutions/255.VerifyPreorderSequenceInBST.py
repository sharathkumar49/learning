"""
255. Verify Preorder Sequence in Binary Search Tree
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

Constraints:
- 1 <= preorder.length <= 10^4
- -10^8 <= preorder[i] <= 10^8
- All the elements of preorder are unique.

Example 1:
Input: preorder = [5,2,1,3,6]
Output: true

Example 2:
Input: preorder = [5,2,6,1,3]
Output: false
"""
def verifyPreorder(preorder):
    stack = []
    low = float('-inf')
    for value in preorder:
        if value < low:
            return False
        while stack and value > stack[-1]:
            low = stack.pop()
        stack.append(value)
    return True

# Example usage:
if __name__ == "__main__":
    print(verifyPreorder([5,2,1,3,6]))   # Output: True
    print(verifyPreorder([5,2,6,1,3]))  # Output: False

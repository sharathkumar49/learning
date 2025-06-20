"""
654. Maximum Binary Tree
Difficulty: Medium

Given an integer array nums, construct a maximum binary tree as per the following rules:
- The root is the maximum number in the array.
- The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
- The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Return the root of the maximum binary tree.

Example 1:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    max_idx = nums.index(max(nums))
    root = TreeNode(nums[max_idx])
    root.left = constructMaximumBinaryTree(nums[:max_idx])
    root.right = constructMaximumBinaryTree(nums[max_idx+1:])
    return root

# Example usage
# (See LeetCode for binary tree construction examples)

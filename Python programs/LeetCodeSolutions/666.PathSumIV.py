"""
LeetCode 666. Path Sum IV

If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
For each integer in this list:
- The hundreds digit represents the depth D of this node, 1 <= D <= 4.
- The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
- The units digit represents the value V of this node, 0 <= V <= 9.

Given a list of ascending three-digits integers representing a binary tree with depth less than 5, you need to return the sum of all paths from the root towards the leaves.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: The tree that the list represents is:
    3
   / \
  5   1
The path sum is (3 + 5) + (3 + 1) = 12.

Constraints:
- The number of nodes in the given list is between 1 and 15.
- 113 <= node.val <= 489

"""
from typing import List

def pathSum(nums: List[int]) -> int:
    tree = {}
    for num in nums:
        d, p, v = num // 100, (num // 10) % 10, num % 10
        tree[(d, p)] = v
    def dfs(d, p, acc):
        key = (d, p)
        if key not in tree:
            return 0
        acc += tree[key]
        left = (d+1, p*2-1)
        right = (d+1, p*2)
        if left not in tree and right not in tree:
            return acc
        return dfs(d+1, p*2-1, acc) + dfs(d+1, p*2, acc)
    return dfs(1, 1, 0)

# Example usage
if __name__ == "__main__":
    print(pathSum([113, 215, 221]))  # Output: 12

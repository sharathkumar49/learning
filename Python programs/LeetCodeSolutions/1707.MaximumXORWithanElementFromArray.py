"""
LeetCode 1707. Maximum XOR With an Element From Array

You are given an array nums and queries where each query is [xi, mi]. For each query, find the maximum XOR of xi with any element in nums not greater than mi. If no such element exists, return -1.

Example 1:
Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]

Constraints:
- 1 <= nums.length, queries.length <= 10^5
- 0 <= nums[i], xi, mi <= 10^9
"""
class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        queries = sorted([(mi, xi, i) for i, (xi, mi) in enumerate(queries)])
        res = [0] * len(queries)
        root = TrieNode()
        def insert(num):
            node = root
            for i in range(31, -1, -1):
                b = (num >> i) & 1
                if b not in node.children:
                    node.children[b] = TrieNode()
                node = node.children[b]
        def query(x):
            node = root
            if not node.children:
                return -1
            ans = 0
            for i in range(31, -1, -1):
                b = (x >> i) & 1
                if 1-b in node.children:
                    ans |= (1 << i)
                    node = node.children[1-b]
                elif b in node.children:
                    node = node.children[b]
                else:
                    return -1
            return ans
        idx = 0
        for mi, xi, qid in queries:
            while idx < len(nums) and nums[idx] <= mi:
                insert(nums[idx])
                idx += 1
            res[qid] = query(xi)
        return res

# Example usage:
# nums = [0,1,2,3,4]
# queries = [[3,1],[1,3],[5,6]]
# print(Solution().maximizeXor(nums, queries))  # Output: [3,3,7]

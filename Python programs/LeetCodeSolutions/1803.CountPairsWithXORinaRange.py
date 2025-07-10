"""
LeetCode 1803. Count Pairs With XOR in a Range

Given an array nums and two integers low and high, return the number of pairs (i, j) with i < j and low <= (nums[i] XOR nums[j]) <= high.

Example 1:
Input: nums = [1,4,2,7], low = 2, high = 6
Output: 6

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 2 * 10^4
- 0 <= low <= high <= 2 * 10^9
"""
class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0

def countPairs(nums, low, high):
    def f(x):
        root = Trie()
        res = 0
        for num in nums:
            node = root
            cnt = 0
            for k in range(14, -1, -1):
                b = (num >> k) & 1
                if x is not None:
                    t = (x >> k) & 1
                    if t:
                        if b^1 in node.children:
                            cnt += node.children[b^1].count
                    if b in node.children:
                        node = node.children[b]
                    else:
                        node = None
                        break
                else:
                    if b not in node.children:
                        node.children[b] = Trie()
                    node = node.children[b]
                    node.count += 1
            if x is not None and node:
                cnt += node.count
            if x is None:
                continue
            res += cnt
        return res
    root = Trie()
    for num in nums:
        node = root
        for k in range(14, -1, -1):
            b = (num >> k) & 1
            if b not in node.children:
                node.children[b] = Trie()
            node = node.children[b]
            node.count += 1
    def count(x):
        res = 0
        for num in nums:
            node = root
            cnt = 0
            for k in range(14, -1, -1):
                b = (num >> k) & 1
                t = (x >> k) & 1
                if t:
                    if b^1 in node.children:
                        cnt += node.children[b^1].count
                if b in node.children:
                    node = node.children[b]
                else:
                    node = None
                    break
            res += cnt
        return res // 2
    return count(high+1) - count(low)

# Example usage:
# nums = [1,4,2,7]
# low = 2
# high = 6
# print(countPairs(nums, low, high))  # Output: 6

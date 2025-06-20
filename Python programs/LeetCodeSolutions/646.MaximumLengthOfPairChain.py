"""
646. Maximum Length of Pair Chain
Difficulty: Medium

You are given an array of n pairs pairs where pairs[i] = [left_i, right_i] and left_i < right_i. A pair [c, d] can follow another pair [a, b] if b < c. Return the length of the longest chain which can be formed.

Example 1:
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2

Constraints:
1 <= pairs.length <= 1000
-1000 <= left_i < right_i <= 1000
"""

def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])
    curr, res = float('-inf'), 0
    for x, y in pairs:
        if x > curr:
            res += 1
            curr = y
    return res

# Example usage
if __name__ == "__main__":
    print(findLongestChain([[1,2],[2,3],[3,4]]))  # Output: 2

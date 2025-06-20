"""
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that only numbers from 1 to 9 are used and each combination should be a unique set of numbers.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Constraints:
- 2 <= k <= 9
- 1 <= n <= 60

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
"""
def combinationSum3(k, n):
    res = []
    def backtrack(start, path, total):
        if len(path) == k and total == n:
            res.append(path[:])
            return
        if len(path) > k or total > n:
            return
        for i in range(start, 10):
            path.append(i)
            backtrack(i+1, path, total+i)
            path.pop()
    backtrack(1, [], 0)
    return res

# Example usage:
if __name__ == "__main__":
    print(combinationSum3(3, 7))  # Output: [[1,2,4]]
    print(combinationSum3(3, 9))  # Output: [[1,2,6],[1,3,5],[2,3,4]]

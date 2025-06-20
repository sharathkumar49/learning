# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
#
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
#
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [[1,2,2],[5]]
#
# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    def backtrack(remain, comb, start):
        if remain == 0:
            res.append(list(comb))
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > remain:
                break
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i+1)
            comb.pop()
    backtrack(target, [], 0)
    return res

# Example usage
candidates = [10,1,2,7,6,1,5]
target = 8
print("Combination Sum II:", combinationSum2(candidates, target))  # Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

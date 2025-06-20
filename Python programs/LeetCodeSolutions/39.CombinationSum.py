# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
# The same number may be chosen from candidates an unlimited number of times.
#
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
#
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

def combinationSum(candidates, target):
    res = []
    def backtrack(remain, comb, start):
        if remain == 0:
            res.append(list(comb))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                continue
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i)
            comb.pop()
    backtrack(target, [], 0)
    return res

# Example usage
candidates = [2,3,6,7]
target = 7
print("Combination Sum:", combinationSum(candidates, target))  # Output: [[2,2,3],[7]]

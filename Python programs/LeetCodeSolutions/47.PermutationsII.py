# 47. Permutations II
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
# Example 1:
# Input: nums = [1,1,2]
# Output: [[1,1,2],[1,2,1],[2,1,1]]
#
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

def permuteUnique(nums):
    res = []
    nums.sort()
    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False]*len(nums))
    return res

# Example usage
nums = [1,1,2]
print("Unique permutations:", permuteUnique(nums))  # Output: [[1,1,2],[1,2,1],[2,1,1]]

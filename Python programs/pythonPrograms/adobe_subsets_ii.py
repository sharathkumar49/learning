# Adobe: Subsets II
# Given a collection of integers that might contain duplicates, return all possible subsets (the power set).

def subsets_with_dup(nums):
    res = []
    nums.sort()
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res

if __name__ == "__main__":
    print(subsets_with_dup([1,2,2]))  # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

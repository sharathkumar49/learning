# Microsoft: Subsets II (Find all unique subsets with duplicates in input)
# Given a collection of integers that might contain duplicates, return all possible subsets (the power set) without duplicate subsets.

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
    arr1 = [1,2,2]
    print(subsets_with_dup(arr1))  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    arr2 = [4,4,4,1,4]
    print(subsets_with_dup(arr2))

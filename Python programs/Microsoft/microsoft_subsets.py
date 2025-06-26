# Microsoft: Subsets (Power Set)
# Given a set of distinct integers, return all possible subsets (the power set).

def subsets(nums):
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res

if __name__ == "__main__":
    arr1 = [1,2,3]
    print(subsets(arr1))  # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    arr2 = [0]
    print(subsets(arr2))  # Output: [[],[0]]

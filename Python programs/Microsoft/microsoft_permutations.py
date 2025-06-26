# Microsoft: Permutations
# Given a collection of distinct integers, return all possible permutations.

def permute(nums):
    res = []
    def backtrack(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False]*len(nums))
    return res

if __name__ == "__main__":
    arr1 = [1,2,3]
    print(permute(arr1))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    arr2 = [0,1]
    print(permute(arr2))  # Output: [[0,1],[1,0]]

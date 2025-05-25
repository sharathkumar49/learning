# Microsoft: Combination Sum
# Given an array of distinct integers candidates and a target integer target, return all unique combinations of candidates where the chosen numbers sum to target.

def combination_sum(candidates, target):
    res = []
    def backtrack(remain, path, start):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                continue
            path.append(candidates[i])
            backtrack(remain - candidates[i], path, i)
            path.pop()
    backtrack(target, [], 0)
    return res

if __name__ == "__main__":
    arr1 = [2,3,6,7]
    target1 = 7
    print(combination_sum(arr1, target1))  # Output: [[2,2,3],[7]]
    arr2 = [2,3,5]
    target2 = 8
    print(combination_sum(arr2, target2))  # Output: [[2,2,2,2],[2,3,3],[3,5]]

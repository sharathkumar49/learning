# Subset sum (find all subsets that sum to a target)
def subset_sum(nums, target):
    res = []
    def backtrack(i, path, total):
        if total == target:
            res.append(path[:])
            return
        if i >= len(nums) or total > target:
            return
        backtrack(i+1, path+[nums[i]], total+nums[i])
        backtrack(i+1, path, total)
    backtrack(0, [], 0)
    return res

if __name__ == "__main__":
    nums = list(map(int, input("Numbers: ").split()))
    target = int(input("Target: "))
    print("Subsets:", subset_sum(nums, target))

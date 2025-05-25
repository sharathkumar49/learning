# Walmart: Subsets
# Given a set of distinct integers, return all possible subsets (the power set).

def subsets(nums):
    res = [[]]
    for n in nums:
        res += [item + [n] for item in res]
    return res

if __name__ == "__main__":
    print(subsets([1,2,3]))  # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

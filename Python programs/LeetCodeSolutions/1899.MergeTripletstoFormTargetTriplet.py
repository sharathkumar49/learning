"""
LeetCode 1899. Merge Triplets to Form Target Triplet

Given a list of triplets and a target triplet, return true if you can select some triplets and merge them to form the target triplet.

Example:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true

Constraints:
- 1 <= triplets.length <= 10^5
- 1 <= triplets[i][j], target[j] <= 1000
"""

def mergeTriplets(triplets, target):
    good = [False, False, False]
    for t in triplets:
        if all(t[i] <= target[i] for i in range(3)):
            for i in range(3):
                if t[i] == target[i]:
                    good[i] = True
    return all(good)

# Example usage:
# print(mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))  # Output: True

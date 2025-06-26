"""
LeetCode 1452. People Whose List of Favorite Companies Is Not a Subset of Another List

Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorite companies for the ith person, return the indices of people whose list of favorite companies is not a subset of any other list. The answer should be returned in any order.

Constraints:
- 1 <= favoriteCompanies.length <= 100
- 1 <= favoriteCompanies[i].length <= 500
- 1 <= favoriteCompanies[i][j].length <= 20

Example:
Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4]
"""
def peopleIndexes(favoriteCompanies):
    sets = [set(fc) for fc in favoriteCompanies]
    res = []
    for i, s in enumerate(sets):
        if not any(s < t for j, t in enumerate(sets) if i != j):
            res.append(i)
    return res

# Example usage:
favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
print(peopleIndexes(favoriteCompanies))  # Output: [0, 1, 4]

"""
LeetCode 1409. Queries on a Permutation With Key

Given the array queries and the integer m, you have a permutation of the integers [1, 2, ..., m] initially. For each query, find the position of the queried number in the permutation, then move this number to the front of the permutation. Return an array of positions for each query.

Constraints:
- 1 <= m <= 10^3
- 1 <= queries.length <= m
- 1 <= queries[i] <= m

Example:
Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1]
"""
def processQueries(queries, m):
    perm = list(range(1, m+1))
    res = []
    for q in queries:
        idx = perm.index(q)
        res.append(idx)
        perm.pop(idx)
        perm = [q] + perm
    return res

# Example usage:
queries = [3,1,2,1]
m = 5
print(processQueries(queries, m))  # Output: [2, 1, 2, 1]

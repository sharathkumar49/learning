"""
1198. Find Smallest Common Element in All Rows

Given a matrix mat where each row is sorted, return the smallest common element in all rows. If no such element exists, return -1.

Constraints:
- 1 <= mat.length, mat[i].length <= 500
- 1 <= mat[i][j] <= 10^4

Example:
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[4,5,8,10,12]]
Output: 4

"""
def smallestCommonElement(mat):
    from collections import Counter
    count = Counter()
    for row in mat:
        count.update(set(row))
    for num in sorted(count):
        if count[num] == len(mat):
            return num
    return -1

# Example usage
if __name__ == "__main__":
    mat = [[1,2,3,4,5],[2,4,5,8,10],[4,5,8,10,12]]
    print(smallestCommonElement(mat))  # Output: 4

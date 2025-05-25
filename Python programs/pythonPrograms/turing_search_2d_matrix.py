# Turing: Search a 2D Matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. Integers in each row are sorted left to right, and the first integer of each row is greater than the last integer of the previous row.

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # Output: True
    print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # Output: False

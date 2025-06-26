# Amazon: Search a 2D Matrix
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
    m = int(input("Rows: "))
    n = int(input("Cols: "))
    matrix = [list(map(int, input().split())) for _ in range(m)]
    target = int(input("Target: "))
    print("Found:", search_matrix(matrix, target))

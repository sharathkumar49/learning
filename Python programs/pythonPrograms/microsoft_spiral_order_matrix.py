# Microsoft: Spiral Order Matrix
# Given a matrix, return all elements of the matrix in spiral order.

def spiral_order(matrix):
    res = []
    if not matrix:
        return res
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
    return res

if __name__ == "__main__":
    mat1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(spiral_order(mat1))  # Output: [1,2,3,6,9,8,7,4,5]
    mat2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    print(spiral_order(mat2))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]

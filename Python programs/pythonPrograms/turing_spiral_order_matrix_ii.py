# Turing: Spiral Order Matrix II
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

def generate_matrix(n):
    res = [[0]*n for _ in range(n)]
    left, right, top, bottom = 0, n-1, 0, n-1
    num = 1
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            res[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom+1):
            res[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                res[i][left] = num
                num += 1
            left += 1
    return res

if __name__ == "__main__":
    print(generate_matrix(3))  # Output: [[1,2,3],[8,9,4],[7,6,5]]
    print(generate_matrix(1))  # Output: [[1]]

"""
661. Image Smoother
Difficulty: Easy

Given an m x n integer matrix img, return the smoothed matrix. Each cell's new value is the average of itself and its neighbors (rounded down).

Example 1:
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]

Constraints:
1 <= m, n <= 200
0 <= img[i][j] <= 255
"""

def imageSmoother(img):
    m, n = len(img), len(img[0])
    res = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            s = 0
            cnt = 0
            for x in range(max(0,i-1), min(m,i+2)):
                for y in range(max(0,j-1), min(n,j+2)):
                    s += img[x][y]
                    cnt += 1
            res[i][j] = s // cnt
    return res

# Example usage
if __name__ == "__main__":
    print(imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))  # Output: [[0,0,0],[0,0,0],[0,0,0]]

"""
832. Flipping an Image

Given an n x n binary matrix image, flip the image horizontally, then invert it.

Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]

Constraints:
- n == image.length
- n == image[i].length
- 1 <= n <= 20
- image[i][j] is 0 or 1.
"""
def flipAndInvertImage(image):
    for row in image:
        row.reverse()
        for i in range(len(row)):
            row[i] ^= 1
    return image

# Example usage:
print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))  # Output: [[1,0,0],[0,1,0],[1,1,1]]

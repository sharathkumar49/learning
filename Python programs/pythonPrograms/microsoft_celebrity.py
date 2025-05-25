# Microsoft: Find the Celebrity (graph/array logic)
# There are n people at a party. If person A knows person B, matrix[A][B] == 1, else 0.
# A celebrity is known by everyone but knows no one. Find the celebrity (return index) or -1 if none.

def find_celebrity(matrix):
    n = len(matrix)
    candidate = 0
    for i in range(1, n):
        if matrix[candidate][i]:
            candidate = i
    for i in range(n):
        if i != candidate:
            if matrix[candidate][i] or not matrix[i][candidate]:
                return -1
    return candidate

if __name__ == "__main__":
    matrix1 = [
        [0,1,1],
        [0,0,1],
        [0,0,0]
    ]
    matrix2 = [
        [0,1,0],
        [0,0,0],
        [1,1,0]
    ]
    print(find_celebrity(matrix1))  # Output: 2
    print(find_celebrity(matrix2))  # Output: 1
    matrix3 = [
        [0,1,0],
        [0,0,1],
        [1,0,0]
    ]
    print(find_celebrity(matrix3))  # Output: -1 (no celebrity)

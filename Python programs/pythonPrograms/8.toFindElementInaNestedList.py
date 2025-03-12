# Sample matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Define the element you want to find
target = 5

# Find the element in the matrix
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"Element {target} found at position ({i}, {j})")
            found = True
            break
    if found:
        break

if not found:
    print(f"Element {target} not found in the matrix")





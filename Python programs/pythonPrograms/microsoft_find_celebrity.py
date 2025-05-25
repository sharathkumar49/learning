# Microsoft: Find the Celebrity (graph)
def find_celebrity(n, knows):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate

# Example knows function for testing
matrix = []
def knows(a, b):
    return matrix[a][b]

if __name__ == "__main__":
    n = int(input("Number of people: "))
    print("Enter the knows matrix (0/1):")
    global matrix
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print("Celebrity:", find_celebrity(n, knows))

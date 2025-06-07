# Problem: Find the celebrity (if any) in a party of n people. 
# Celebrity Definition: Everyone knows the celebrity, but the
# celebrity knows no one.


def find_celebrity(matrix):
    stack = [i for i in range(len(matrix))]
    print("Initial stack:", stack)

    while len(stack) > 1:
        a = stack.pop()
        print("Popped a:", a)
        b = stack.pop()
        print("Popped b:", b)
        print("Comparing a and b:", a, b)
        if matrix[a][b]:  
            print(matrix[a][b], "means a knows b")
            stack.append(b)  # a knows b, a is not celebrity
        else:
            print(matrix[a][b], "means a doesn't know b")
            stack.append(a)  # a doesn't know b, b is not celebrity

    candidate = stack.pop()
    if all(matrix[i][candidate] for i in range(len(matrix)) if i != candidate) and \
       all(not matrix[candidate][i] for i in range(len(matrix))):
        return candidate
    return -1

# Example Party Matrix
party = [[0, 1, 1], 
         [0, 0, 1], 
         [0, 0, 0]]
print(find_celebrity(party))  # 2

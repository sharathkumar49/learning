

def right_triangle(n):
    for i in range(1, n + 1):  # Loop through each row
        for j in range(i):  # Loop through each column in the current row
            print("*", end=" ")  # Print star followed by a space
        print()  # Move to the next line after each row


# Driver Code
n = 5
right_triangle(n)

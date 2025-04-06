
def left_triangle(n):
    for i in range(1, n + 1):  # Loop through each row
        for j in range(n - i):  # Print spaces before stars
            print(" ", end=" ")
        for j in range(i):  # Print stars
            print("* ", end=" ")
        print()  # Move to the next line after each row

# Driver Code
n = 5
left_triangle(n)

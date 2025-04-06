def centered_triangle(n):

    for i in range(1, n + 1):  # Outer loop to handle number of rows 
 
        for j in range(0, n- i + 1):  # Inner loop to handle number of spaces 
            print(end=" ")

        for j in range(0, i):  # Inner loop to handle number of stars 
            print("* ", end="")  # Printing stars
        print()  # Ending line after each row

# Driver Code
n = 5
centered_triangle(n)



# without including the spaces, it will produce left sided triangle

# def centered_triangle(n):
#     k = n - 1  # Number of spaces

#     for i in range(0, n):  # Outer loop to handle number of rows
#         for j in range(0, k):  # Inner loop to handle number of spaces
#             print(end=" ")
#         k = k - 1  # Decrementing k after each loop

#         for j in range(0, i + 1):  # Inner loop to handle number of columns
#             print("*", end="")  # Printing stars without spaces

#         print()  # Ending line after each row

# # Driver Code
# n = 5
# centered_triangle(n)

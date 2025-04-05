# Source :  https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/

#copy the code and run it in pycharm for better understanding
def pypart2(n):

    # number of spaces
    k = 2 * n - 2
    print("If the value of n is 5, the corresponding matrix is 5 X 5, since we are adding space in-between the asterisks, We need 10 X 10.")
    print("So, having 1 asterisk(*) means, we are accommodating 2 values in that corresponding row, one for asterisk(*) and one for a space.")
    print("Here we are having right side triangle, we are having spaces first then asterisk and space duet.")
    print("In the row 1, both(* and a space) accommodate 2 values, and for accomodating")
    print("remaining 8 values, we multiplying rows * 2, which gives us 10 and decrementing 2")
    print("which gives us 8, that's why --> k = 2 * n -2")
    print("and decrementing 2 from k each time, at the end each for loop(space), k = k - 2 ")
    print("\n\n")

    # outer loop to handle number of rows
    for i in range(0, n):

        for j in range(0, k): #inner loop to handle number spaces values changing acc. to requirement
            print(end="S")
        print("The number of spaces printed ", j+1)
        print("now let's decrement the value of k for next iteration")
        k = k - 2 #decrementing k after each loop
        print("the value of k = k - 2 = ", k)

        for j in range(0, i + 1): # inner loop to handle number of columns values changing acc. to outer loop
            print("*D", end="") # printing stars
        print("The number of stars printed ", j)
        print("\r") #ending line after each row


# Driver Code
n = 5
pypart2(n)





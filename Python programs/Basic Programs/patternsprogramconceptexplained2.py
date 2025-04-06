#Function to demonstrate printing pattern
#For more clarification, visit patternsprogramconceptexplained file
def pypart2(n):
	
	k = 2*n - 2      # number of spaces
	for i in range(0, n):  # outer loop to handle number of rows

		for j in range(0, k): #inner loop to handle number spaces values changing acc. to requirement
			print(end=" ")   #printing spaces

		k = k - 2     #decrementing k after each loop
	
		for j in range(0, i+1):  # inner loop to handle number of columns values changing acc. to outer loop
			print("* ", end="")  # printing stars

		print("\r")   # ending line after each row

# Driver Code
n = 5
pypart2(n)

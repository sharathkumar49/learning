#using the loops in python, we can print different patterns in python
# using for loop
# Function to demonstrate printing pattern
print("\nusing for loops(i, j), left most pattern")
def pypattern(n):
	
	for i in range(0, n):  #outer loop to handle number of rows, n in this case
	
		for j in range(0, i+1):  #inner loop to handle number of columns, values will be changing acc. to outer loop
			print("* ",end="")  #printing stars
	
		print("\r")   #ending line after each row

# Driver Code
n = 5
pypattern(n)




print("\nusing stack, left most pattern")
#Another Approach: 
#Using List, this could be done in a simpler way
# Function to demonstrate printing pattern
def pypart(n):
	myList = []

	for i in range(1,n+1):
		myList.append("* "*i)

	print("\n".join(myList))

# Driver Code
n = 5
pypart(n)


print("\n using for loops(i,j), rightmost pattern")
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




print("\ncentralized pattern")

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	k = n - 1  #number of spaces

	for i in range(0, n): # outer loop to handle number of rows
	
		for j in range(0, k):  # inner loop to handle number spaces values changing acc. to requirement
			print(end=" ")

		k = k - 1  #decrementing k after each loop

		for j in range(0, i+1):  #inner loop to handle number of columns values changing acc. to outer loop
			print("* ", end="")  #printing stars

		print("\r")     #ending line after each row


# Driver Code
n = 5
triangle(n)



# Function to demonstrate printing pattern of numbers
def numpat(n):
	
	num = 1  #initialising starting number,  note: even if comment this, you'd get the same output 

	for i in range(0, n):   #outer loop to handle number of rows
	
		num = 1  #re assigning num ,      note: but if you comment this, number will printed as per the last assigned value
	
		for j in range(0, i+1):  #inner loop to handle number of columns, values will change acc. to outer loop
			
			print(num, end=" ")  #printing number
			num = num + 1  #incrementing number at each column
	
		print("\r")   #ending line after each row

# Driver code
n = 5
numpat(n)



#Numbers without reassigning
# Function to demonstrate printing pattern of numbers
def contnum(n):
	
	num = 1 #initializing starting number

	for i in range(0, n):   #outer loop to handle number of rows
	
		# not re assigning num
		# num = 1
	
		for j in range(0, i+1): #inner loop to handle number of columns, values will change acc. to outer loop
			print(num, end=" ")  #printing number
			num = num + 1   #incrementing number at each column
	
		print("\r")   #ending line after each row

#driver code
n = 5
# sending 5 as argument
# calling Function
contnum(n)





# Function to demonstrate printing pattern of alphabets
def alphapat(n):
	
	num = 65  #initializing value corresponding to 'A' ASCII value

	for i in range(0, n):  #outer loop to handle number of rows, 5 in this case
	
		for j in range(0, i+1):  #inner loop to handle number of columns, values will change acc. to outer loop
			ch = chr(num)  #explicitly converting to char
			print(ch, end=" ")  #printing char value
	
		num = num + 1   #incrementing number
		print("\r")  #ending line after each row

# Driver Code
n = 5
alphapat(n)




#Continuous Character pattern
#Function to demonstrate printing pattern of alphabets
def contalpha(n):
	
	num = 65  # initializing value corresponding to 'A' ASCII value

	for i in range(0, n):  #outer loop to handle number of rows
      
         for j in range(0, i+1):   #inner loop to handle number of columns, values will change acc. to outer loop
         
            ch = chr(num)  #explicitly converting to char
            print(ch, end=" ") #printing char value
            num = num +1  #incrementing at each column
    
         print("\r")  #ending line after each row
 
# Driver code
n = 5
contalpha(n)    





# In a peaceful kingdom, there are houses numbered from 1 to n. 
# The king announces a prize of gold coins to some special group of houses. 
# You have been given the task to determine how many sets of three houses 
# can form a special group, where the sum of the square of two smaller house numbers 
# is equal to the square of the largest house number


# Solution: 
# This problem is essentially finding sets of three numbers (a, b, c) that satisfy the Pythagorean theorem:
# a² + b² = c²

def count_special_groups(n):
	special_groups = []
	
	for a in range(1, n+1):
		for b in range(a, n+1):
			c_squared = a**2 + b**2
			c = int(c_squared**0.5)
			if c<=n and c**2 == c_squared:
				special_groups.append((a,b,c))
				
	return special_groups
	
	
#Example Usage
# n = int(input("Enter the value of n: "))
n = 10
special_groups = count_special_groups(n)
print(f"Number of special groups: {len(special_groups)}")
print("special groups: ", special_groups)


# To print the combination of duplicates also, say (a, b, c) and (b, a, c) as separate groups:

def count_special_groups(n):
	special_groups = []
	
	for a in range(1, n+1): 
		for b in range(1, n+1):
			c_squared = a**2 + b**2
			c = int(c_squared**0.5)
			if c <= n and c**2 == c_squared:
				special_groups.append((a,b,c))
				
	return special_groups
	
	
#Example Usage
# n = int(input("Enter the value of n: "))
n = 10
special_groups = count_special_groups(n)
print(f"Number of special groups: {len(special_groups)}")
print("special groups: ", special_groups)




# smart_parcel_sorting:
# you work at a delivery company where packages of various weights arrive randomly. 
# You must sort them into groups such that each group has packages weighing no more 
# than a given limit 'max_weight'


# Method 1: 
def min_parcel_groups(parcels, max_weight):
    parcels.sort(reverse=True)
    groups = 0
    
    while parcels:
        current = parcels.pop(0)
        
        # Find the largest parcel that can be paired with 'current'
        index = -1
        for i in range(len(parcels)):
            if parcels[i] <= max_weight - current:
                index = i
                break
        
        # If found, remove it from the list
        if index != -1:
            parcels.pop(index)
        
        groups += 1
    
    return groups

# Example usage
parcels = [5, 12, 8, 7, 14, 10]
max_weight = 15
print("Minimum parcel groups:", min_parcel_groups(parcels, max_weight))






# Method 2:

# Another approach to solving this problem is using a two-pointer technique instead of sorting and manually searching. This method works efficiently by pairing the lightest and heaviest packages available.

# Here’s how it works:
# 1. Sort the parcels in ascending order.
# 2. Use two pointers—one at the beginning (lightest package) and one at the end (heaviest package).
# 3. Try to form the heaviest valid pair possible by adding the smallest package to the largest.
# 4. If the sum is within 'max_weight', remove both parcels from the list.
# 5. Otherwise, remove only the heaviest package.
# 6. Continue until all parcels are grouped.

# Implementation:

def min_parcel_groups(parcels, max_weight):
    parcels.sort()
    left, right = 0, len(parcels) - 1
    groups = 0

    while left <= right:
        if parcels[left] + parcels[right] <= max_weight:
            left += 1  # Pair found, move left pointer
        right -= 1  # Largest parcel always removed
        groups += 1

    return groups

# Example usage
parcels = [5, 12, 8, 7, 14, 10]
max_weight = 15
print("Minimum parcel groups:", min_parcel_groups(parcels, max_weight))


# This approach efficiently finds the minimum number of groups in O(n log n) time due to sorting, followed by an O(n) pairing process. It minimizes the number of groups by optimally pairing parcels whenever possible.

# Let's walk through the two-pointer approach step by step, using the example parcels:

# Given:

# parcels = [5, 12, 8, 7, 14, 10]
# max_weight = 15


# Step 1: Sort the parcels in ascending order
# Sorting makes it easier to find the lightest and heaviest packages efficiently.

# Sorted parcels: [5, 7, 8, 10, 12, 14]

# Now, we use two pointers:
# - 'left' starts at index 0 (smallest package: '5').
# - 'right' starts at index 5 (largest package: '14').

# Step 2: Pair packages optimally
# We always try to pair the largest available package with the smallest one—only if their sum is within 'max_weight'.

# First Iteration: '5 + 14 = 19' (Too heavy)
# - Since pairing isn’t possible, we remove only the largest package ('14').
# - 'right' moves to index 4 ('12').
# - Groups so far: '1'

# Second Iteration: '5 + 12 = 17' (Too heavy)
# - Again, pairing isn’t possible, so we remove the largest package ('12').
# - 'right' moves to index 3 ('10').
# - Groups so far: '2'


# Third Iteration: '5 + 10 = 15' (Valid Pair!)
# - Since pairing is possible, we remove both packages ('5' and '10').
# - 'left' moves to index 1 ('7').
# - 'right' moves to index 2 ('8').
# - Groups so far: '3'

# Fourth Iteration: '7 + 8 = 15' (Valid Pair!)
# - Since pairing is possible, we remove both packages ('7' and '8').
# - Groups so far: '4'


# Step 3: All packages sorted!
# Since all parcels have been grouped optimally, the final minimum number of groups is 4.

# Why is this approach better?
# ✅ Avoids unnecessary searching (compared to a manual search method).  
# ✅ Uses O(n log n) for sorting, then O(n) for pairing, making it efficient.  
# ✅ Finds the optimal pair without using built-in functions like 'bisect_right'. 










# Method 3:
from bisect import bisect_right

def min_parcel_groups(parcels, max_weight):
	# parcels.sort(reverse=True)
	parcels.sort() 
	groups = 0
	while parcels:
		current = parcels.pop(0)
		index = bisect_right(parcels, max_weight - current)
		if index > 0:
			parcels.pop(index - 1)
		groups += 1
	return groups
	
	
#Example usage
parcels = [5, 12, 8, 7, 14, 10]
max_weight = 15
print("Minimum parcel groups:", min_parcel_groups(parcels, max_weight)) 

# This method uses the bisect module to find the index of the largest parcel that can be paired with 'current' efficiently.
# It has a time complexity of O(n log n) due to sorting and binary search, making it efficient for larger datasets.

# This method is particularly useful when the list of parcels is large, as it reduces the time complexity of finding the index to O(log n) using binary search.
# The overall complexity remains O(n log n) due to the initial sorting step.
# This is a good balance between readability and performance, especially for larger datasets.

# In summary, the two-pointer technique is a great way to solve the parcel sorting problem efficiently.
# It minimizes the number of groups by optimally pairing parcels whenever possible.	
# The method is efficient, easy to understand, and can be adapted for various constraints or requirements.
# You can choose
# the method that best fits your needs based on the size of the dataset and the specific requirements of your application.
# Happy coding!
	

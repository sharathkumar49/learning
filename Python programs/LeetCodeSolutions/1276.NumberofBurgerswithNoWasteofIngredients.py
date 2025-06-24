"""
LeetCode 1276. Number of Burgers with No Waste of Ingredients

Given the number of tomato slices and cheese slices, return the number of jumbo and small burgers that can be made. Jumbo uses 4 tomato slices, small uses 2. Return [] if no solution exists.

Constraints:
- 0 <= tomatoSlices <= 10^7
- 0 <= cheeseSlices <= 10^7

Example:
Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
"""
def numOfBurgers(tomatoSlices, cheeseSlices):
    j = tomatoSlices - 2 * cheeseSlices
    if j < 0 or j % 2 != 0:
        return []
    jumbo = j // 2
    small = cheeseSlices - jumbo
    if jumbo < 0 or small < 0:
        return []
    return [jumbo, small]

# Example usage:
print(numOfBurgers(16, 7))  # Output: [1, 6]

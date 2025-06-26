"""
LeetCode 1431. Kids With the Greatest Number of Candies

Given the array candies and the integer extraCandies, return a boolean list indicating whether each child can have the greatest number of candies after taking the extraCandies.

Constraints:
- 2 <= candies.length <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50

Example:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
"""
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [c + extraCandies >= max_candies for c in candies]

# Example usage:
candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]

"""
LeetCode 2107. Number of Unique Flavors After Sharing K Candies

Given an array candies and an integer k, return the number of unique flavors after sharing k candies.

Example:
Input: candies = [1,1,2,2,3,3], k = 2
Output: 2

Constraints:
- 1 <= candies.length <= 10^5
- 1 <= candies[i] <= 10^5
- 0 <= k <= candies.length
"""

def shareCandies(candies, k):
    from collections import Counter
    n = len(candies)
    count = Counter(candies)
    min_unique = float('inf')
    for i in range(n-k+1):
        window = candies[i:i+k]
        unique = len(set(candies) - set(window))
        min_unique = min(min_unique, unique)
    return min_unique

# Example usage:
# print(shareCandies([1,1,2,2,3,3], 2))  # Output: 2

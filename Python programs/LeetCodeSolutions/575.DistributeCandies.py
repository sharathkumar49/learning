"""
575. Distribute Candies
Difficulty: Easy

Alice has n candies, where each candy is of a different kind numbered 1 to n. She wants to distribute the candies equally between herself and her sister. Return the maximum number of kinds of candies Alice can eat.

Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3

Example 2:
Input: candyType = [1,1,2,3]
Output: 2

Constraints:
2 <= candyType.length <= 10^4
candyType.length is even.
-10^5 <= candyType[i] <= 10^5
"""

def distributeCandies(candyType):
    return min(len(set(candyType)), len(candyType)//2)

# Example usage
if __name__ == "__main__":
    print(distributeCandies([1,1,2,2,3,3]))  # Output: 3
    print(distributeCandies([1,1,2,3]))      # Output: 2

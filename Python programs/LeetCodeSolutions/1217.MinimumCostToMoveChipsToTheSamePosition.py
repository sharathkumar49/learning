"""
1217. Minimum Cost to Move Chips to The Same Position

Given an array position, return the minimum cost to move all chips to the same position. Moving a chip by 2 is free, by 1 costs 1.

Constraints:
- 1 <= position.length <= 100
- 1 <= position[i] <= 10^9

Example:
Input: position = [1,2,3]
Output: 1

"""
def minCostToMoveChips(position):
    even = sum(1 for x in position if x % 2 == 0)
    odd = len(position) - even
    return min(even, odd)

# Example usage
if __name__ == "__main__":
    print(minCostToMoveChips([1,2,3]))  # Output: 1

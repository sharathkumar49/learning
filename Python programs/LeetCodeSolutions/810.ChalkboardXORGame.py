"""
810. Chalkboard XOR Game

You are given an array of integers nums. Two players take turns removing an element from the array. If the XOR of all the remaining elements is 0 after a player's turn, that player wins. Return true if and only if the first player can win with optimal play.

Example 1:
Input: nums = [1,1,2]
Output: false

Example 2:
Input: nums = [0,1]
Output: true

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] < 2^16
"""
def xorGame(nums):
    from functools import reduce
    return len(nums) % 2 == 0 or reduce(lambda x, y: x ^ y, nums) == 0

# Example usage:
print(xorGame([1,1,2]))  # Output: False
print(xorGame([0,1]))    # Output: True

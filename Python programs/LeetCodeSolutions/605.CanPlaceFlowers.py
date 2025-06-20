"""
605. Can Place Flowers
Difficulty: Easy

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule, and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
            i += 1
        i += 1
    return count >= n

# Example usage
if __name__ == "__main__":
    print(canPlaceFlowers([1,0,0,0,1], 1))  # Output: True
    print(canPlaceFlowers([1,0,0,0,1], 2))  # Output: False

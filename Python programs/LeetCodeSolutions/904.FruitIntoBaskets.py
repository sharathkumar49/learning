"""
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to collect as much fruit as possible, but you only have two baskets, and each basket can only hold a single type of fruit.
Return the length of the longest subarray with at most two different types of fruit.

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length

Example:
Input: fruits = [1,2,1]
Output: 3
"""
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        res = 0
        for right, fruit in enumerate(fruits):
            count[fruit] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            res = max(res, right - left + 1)
        return res

# Example usage
if __name__ == "__main__":
    fruits = [1,2,1]
    print(Solution().totalFruit(fruits))  # Output: 3

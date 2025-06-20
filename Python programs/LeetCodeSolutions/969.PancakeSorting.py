"""
969. Pancake Sorting
https://leetcode.com/problems/pancake-sorting/

Given an array of integers arr, sort the array by performing a series of pancake flips. Return the k-values of the flips performed so that the array becomes sorted in ascending order.

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= arr.length
- All elements are unique.

Example:
Input: arr = [3,2,4,1]
Output: [4,2,4,3]
"""
from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for x in range(n, 1, -1):
            i = arr.index(x)
            if i != x-1:
                if i != 0:
                    res.append(i+1)
                    arr[:i+1] = arr[:i+1][::-1]
                res.append(x)
                arr[:x] = arr[:x][::-1]
        return res

# Example usage
if __name__ == "__main__":
    arr = [3,2,4,1]
    print(Solution().pancakeSort(arr))  # Output: [4,2,4,3]

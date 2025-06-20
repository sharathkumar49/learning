"""
989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/

The array-form of an integer num is an array representing its digits in left to right order. Given num and an integer k, return the array-form of the integer num + k.

Constraints:
- 1 <= num.length <= 10^4
- 0 <= num[i] <= 9
- 0 <= k <= 10^4

Example:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
"""
from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        res = []
        i = n - 1
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
            res.append(k % 10)
            k //= 10
            i -= 1
        return res[::-1]

# Example usage
if __name__ == "__main__":
    num = [1,2,0,0]
    k = 34
    print(Solution().addToArrayForm(num, k))  # Output: [1,2,3,4]

"""
927. Three Equal Parts
https://leetcode.com/problems/three-equal-parts/

Given an array arr of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value (leading zeros allowed), and return any such indices. If it is not possible, return [-1, -1].

Constraints:
- 3 <= arr.length <= 3 * 10^4
- arr[i] is 0 or 1

Example:
Input: arr = [1,0,1,0,1]
Output: [0,3]
"""
from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        S = sum(arr)
        if S % 3 != 0:
            return [-1, -1]
        if S == 0:
            return [0, len(arr)-1]
        k = S // 3
        first = second = third = cur = 0
        for i, x in enumerate(arr):
            if x:
                cur += 1
                if cur == 1:
                    first = i
                elif cur == k+1:
                    second = i
                elif cur == 2*k+1:
                    third = i
        n = len(arr)
        while third < n and arr[first] == arr[second] == arr[third]:
            first += 1
            second += 1
            third += 1
        if third == n:
            return [first-1, second]
        return [-1, -1]

# Example usage
if __name__ == "__main__":
    arr = [1,0,1,0,1]
    print(Solution().threeEqualParts(arr))  # Output: [0,3]

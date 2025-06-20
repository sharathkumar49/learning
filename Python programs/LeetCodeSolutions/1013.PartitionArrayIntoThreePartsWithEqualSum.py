"""
1013. Partition Array Into Three Parts With Equal Sum

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sum.

Constraints:
- 3 <= arr.length <= 5 * 10^4
- -10^4 <= arr[i] <= 10^4

Example:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: [0,2,1], [-6,6,-7,9], [1,2,0,1] all have a sum of 3.
"""
from typing import List

def canThreePartsEqualSum(arr: List[int]) -> bool:
    s = sum(arr)
    if s % 3 != 0:
        return False
    target = s // 3
    cnt, curr = 0, 0
    for num in arr:
        curr += num
        if curr == target:
            cnt += 1
            curr = 0
    return cnt >= 3

# Example usage:
arr = [0,2,1,-6,6,-7,9,1,2,0,1]
print(canThreePartsEqualSum(arr))  # Output: True

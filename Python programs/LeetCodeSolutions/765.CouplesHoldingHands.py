"""
LeetCode 765. Couples Holding Hands

N couples sit in 2N seats arranged in a row and want to hold hands. The people and seats are represented by an integer array row where row[i] is the person sitting in the i-th seat.
Return the minimum number of swaps so that every couple is sitting side by side.

Example 1:
Input: row = [0,2,1,3]
Output: 1

Example 2:
Input: row = [3,2,0,1]
Output: 0

Constraints:
- 2 <= row.length <= 60
- row.length is even.
- 0 <= row[i] < row.length
- All the elements of row are unique.
"""
from typing import List

def minSwapsCouples(row: List[int]) -> int:
    n = len(row)
    pos = {x: i for i, x in enumerate(row)}
    swaps = 0
    for i in range(0, n, 2):
        x, y = row[i], row[i]^1
        if row[i+1] != y:
            j = pos[y]
            row[i+1], row[j] = row[j], row[i+1]
            pos[row[j]] = j
            pos[row[i+1]] = i+1
            swaps += 1
    return swaps

# Example usage
if __name__ == "__main__":
    print(minSwapsCouples([0,2,1,3]))  # Output: 1
    print(minSwapsCouples([3,2,0,1]))  # Output: 0

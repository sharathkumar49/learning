"""
1054. Distant Barcodes

Given an array of barcodes, rearrange the barcodes so that no two adjacent barcodes are equal. Return any such arrangement.

Constraints:
- 1 <= barcodes.length <= 10000
- 1 <= barcodes[i] <= 10000

Example:
Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
"""
from typing import List
from collections import Counter

def rearrangeBarcodes(barcodes: List[int]) -> List[int]:
    count = Counter(barcodes)
    res = [0] * len(barcodes)
    i = 0
    for num, freq in count.most_common():
        for _ in range(freq):
            res[i] = num
            i += 2
            if i >= len(barcodes):
                i = 1
    return res

# Example usage:
barcodes = [1,1,1,2,2,2]
print(rearrangeBarcodes(barcodes))  # Output: [2, 1, 2, 1, 2, 1]

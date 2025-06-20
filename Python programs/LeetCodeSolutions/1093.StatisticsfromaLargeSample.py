"""
1093. Statistics from a Large Sample

You are given a list count where count[i] is the number of occurrences of the integer i. Return the minimum, maximum, mean, median, and mode of the sample.

Constraints:
- count.length == 256
- 0 <= count[i] <= 10^9
- 1 <= sum(count) <= 10^9

Example:
Input: count = [0,1,3,4,0,0,...]
Output: [1.00000, 3.00000, 2.37500, 2.50000, 3.00000]
"""
from typing import List

def sampleStats(count: List[int]) -> List[float]:
    n = sum(count)
    minimum = next(i for i, c in enumerate(count) if c)
    maximum = max(i for i, c in enumerate(count) if c)
    mean = sum(i * c for i, c in enumerate(count)) / n
    mode = count.index(max(count))
    # Median
    total = 0
    m1 = m2 = None
    for i, c in enumerate(count):
        total += c
        if m1 is None and total >= (n + 1) // 2:
            m1 = i
        if m2 is None and total >= (n + 2) // 2:
            m2 = i
            break
    median = (m1 + m2) / 2
    return [float(minimum), float(maximum), mean, median, float(mode)]

# Example usage:
count = [0,1,3,4] + [0]*252
print([f"{x:.5f}" for x in sampleStats(count)])  # Output: ['1.00000', '3.00000', '2.37500', '2.50000', '3.00000']

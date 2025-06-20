"""
LeetCode 683. K Empty Slots

You have n bulbs in a row numbered from 1 to n. Each day, one bulb is turned on. Given an array bulbs, where bulbs[i] = x means that on day i+1, bulb at position x turns on.

Return the earliest day there exists two turned on bulbs with exactly k bulbs between them that are all turned off. If no such day exists, return -1.

Example 1:
Input: bulbs = [1,3,2], k = 1
Output: 2

Example 2:
Input: bulbs = [1,2,3], k = 1
Output: -1

Constraints:
- 1 <= n <= 2 * 10^4
- bulbs is a permutation of [1, 2, ..., n]
- 0 <= k <= 2 * 10^4
"""
from typing import List

def kEmptySlots(bulbs: List[int], k: int) -> int:
    n = len(bulbs)
    days = [0] * n
    for day, pos in enumerate(bulbs):
        days[pos-1] = day + 1
    res = float('inf')
    left, right = 0, k + 1
    while right < n:
        valid = True
        for i in range(left+1, right):
            if days[i] < max(days[left], days[right]):
                left = i
                right = i + k + 1
                valid = False
                break
        if valid:
            res = min(res, max(days[left], days[right]))
            left += 1
            right += 1
    return res if res != float('inf') else -1

# Example usage
if __name__ == "__main__":
    print(kEmptySlots([1,3,2], 1))  # Output: 2
    print(kEmptySlots([1,2,3], 1))  # Output: -1

"""
975. Odd Even Jump
https://leetcode.com/problems/odd-even-jump/

You are given an integer array arr. From some starting index, you can make a series of jumps. The jumps are odd-numbered or even-numbered, and the rules for each are:
- Odd jumps: jump to the smallest index j > i such that arr[j] >= arr[i]
- Even jumps: jump to the smallest index j > i such that arr[j] <= arr[i]
Return the number of good starting indices.

Constraints:
- 1 <= arr.length <= 2 * 10^4
- 0 <= arr[i] < 10^5

Example:
Input: arr = [10,13,12,14,15]
Output: 2
"""
from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        idxs = sorted(range(n), key=lambda i: (arr[i], i))
        stack = []
        next_higher = [0] * n
        for i in idxs:
            while stack and i > stack[-1]:
                next_higher[stack.pop()] = i
            stack.append(i)
        idxs = sorted(range(n), key=lambda i: (-arr[i], i))
        stack = []
        next_lower = [0] * n
        for i in idxs:
            while stack and i > stack[-1]:
                next_lower[stack.pop()] = i
            stack.append(i)
        for i in range(n-2, -1, -1):
            odd[i] = even[next_higher[i]] if next_higher[i] else False
            even[i] = odd[next_lower[i]] if next_lower[i] else False
        return sum(odd)

# Example usage
if __name__ == "__main__":
    arr = [10,13,12,14,15]
    print(Solution().oddEvenJumps(arr))  # Output: 2

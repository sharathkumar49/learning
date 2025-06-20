"""
949. Largest Time for Given Digits
https://leetcode.com/problems/largest-time-for-given-digits/

Given an array arr of 4 digits, return the largest 24-hour time that can be made. If no valid time can be made, return "".

Constraints:
- arr.length == 4
- 0 <= arr[i] <= 9

Example:
Input: arr = [1,2,3,4]
Output: "23:41"
"""
from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1
        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if 0 <= hour < 24 and 0 <= minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        if max_time == -1:
            return ""
        return f"{max_time // 60:02d}:{max_time % 60:02d}"

# Example usage
if __name__ == "__main__":
    arr = [1,2,3,4]
    print(Solution().largestTimeFromDigits(arr))  # Output: "23:41"

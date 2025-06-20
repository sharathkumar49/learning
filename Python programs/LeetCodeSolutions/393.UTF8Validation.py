"""
393. UTF-8 Validation

Given an integer array data representing the data, return true if it is a valid UTF-8 encoding, or false otherwise.

Constraints:
- 1 <= data.length <= 4 * 10^4
- 0 <= data[i] <= 255
"""
from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            byte = data[i]
            if byte & 0x80 == 0:
                cnt = 1
            elif byte & 0xE0 == 0xC0:
                cnt = 2
            elif byte & 0xF0 == 0xE0:
                cnt = 3
            elif byte & 0xF8 == 0xF0:
                cnt = 4
            else:
                return False
            if i + cnt > n:
                return False
            for j in range(1, cnt):
                if data[i + j] & 0xC0 != 0x80:
                    return False
            i += cnt
        return True

# Example usage:
data = [197,130,1]
print(Solution().validUtf8(data))  # Output: True

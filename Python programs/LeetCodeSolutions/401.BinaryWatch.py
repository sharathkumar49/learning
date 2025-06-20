"""
401. Binary Watch

A binary watch has 4 LEDs on the top representing the hours (0-11), and 6 LEDs on the bottom representing the minutes (0-59). Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Constraints:
- 0 <= turnedOn <= 10
"""
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res

# Example usage:
turnedOn = 1
print(Solution().readBinaryWatch(turnedOn))  # Output: ["0:01","0:02",...]

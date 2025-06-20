"""
1010. Pairs of Songs With Total Durations Divisible by 60

Given an array of integers time where time[i] describes the duration of the i-th song, return the number of pairs of songs for which their total duration in seconds is divisible by 60.

Constraints:
- 1 <= time.length <= 6 * 10^4
- 1 <= time[i] <= 500

Example:
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60: (30,150), (20,100), (20,40)
"""
from typing import List

def numPairsDivisibleBy60(time: List[int]) -> int:
    count = [0] * 60
    res = 0
    for t in time:
        res += count[-t % 60]
        count[t % 60] += 1
    return res

# Example usage:
time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))  # Output: 3

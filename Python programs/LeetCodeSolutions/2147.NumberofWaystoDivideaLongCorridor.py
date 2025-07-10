"""
LeetCode 2147. Number of Ways to Divide a Long Corridor

You are given a string corridor representing a long corridor, where corridor[i] is either 'S' (seat) or 'P' (plant). Return the number of ways to divide the corridor into sections such that each section has exactly two seats. Return the answer modulo 10^9 + 7.

Example:
Input: corridor = "SSPSSPSS"
Output: 4

Constraints:
- 1 <= corridor.length <= 10^5
- corridor[i] is either 'S' or 'P'.
"""

def numberOfWays(corridor):
    MOD = 10**9+7
    seats = [i for i, c in enumerate(corridor) if c == 'S']
    if len(seats) == 0 or len(seats) % 2:
        return 0
    res = 1
    for i in range(2, len(seats), 2):
        res = res * (seats[i] - seats[i-1]) % MOD
    return res

# Example usage:
# print(numberOfWays("SSPSSPSS"))  # Output: 4

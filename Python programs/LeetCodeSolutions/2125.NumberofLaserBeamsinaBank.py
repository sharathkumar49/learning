"""
LeetCode 2125. Number of Laser Beams in a Bank

Given a binary string array bank, return the total number of laser beams in the bank.

Example:
Input: bank = ["011001","000000","010100","001000"]
Output: 8

Constraints:
- 1 <= bank.length, bank[i].length <= 10^5
- bank[i][j] is '0' or '1'
"""

def numberOfBeams(bank):
    prev = 0
    res = 0
    for row in bank:
        cnt = row.count('1')
        if cnt:
            res += prev * cnt
            prev = cnt
    return res

# Example usage:
# print(numberOfBeams(["011001","000000","010100","001000"]))  # Output: 8

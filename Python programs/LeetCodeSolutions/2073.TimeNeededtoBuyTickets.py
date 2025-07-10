"""
LeetCode 2073. Time Needed to Buy Tickets

Given an array tickets where tickets[i] is the number of tickets person i needs, and an integer k, return the time needed for the k-th person to buy all their tickets.

Example:
Input: tickets = [2,3,2], k = 2
Output: 6

Constraints:
- n == tickets.length
- 1 <= n <= 100
- 1 <= tickets[i] <= 100
- 0 <= k < n
"""

def timeRequiredToBuy(tickets, k):
    res = 0
    for i, t in enumerate(tickets):
        if i <= k:
            res += min(t, tickets[k])
        else:
            res += min(t, tickets[k]-1)
    return res

# Example usage:
# print(timeRequiredToBuy([2,3,2], 2))  # Output: 6

"""
LeetCode 2409. Count Days Spent Together

Given arrival and departure dates for two people, return the number of days spent together.

Constraints:
- Dates in MM-DD format
"""

def countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob):
    from datetime import datetime
    fmt = "%m-%d"
    start = max(datetime.strptime(arriveAlice, fmt), datetime.strptime(arriveBob, fmt))
    end = min(datetime.strptime(leaveAlice, fmt), datetime.strptime(leaveBob, fmt))
    return max(0, (end-start).days+1)

# Example usage:
# print(countDaysTogether("08-15","08-18","08-16","08-19"))  # Output: 3

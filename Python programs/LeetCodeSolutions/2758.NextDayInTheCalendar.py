"""
LeetCode 2758. Next Day in the Calendar

Given date, return the next day in the calendar.

Constraints:
- 1 <= date.length <= 10^5
"""

def nextDay(date):
    from datetime import datetime, timedelta
    d = datetime.strptime(date, "%Y-%m-%d")
    d += timedelta(days=1)
    return d.strftime("%Y-%m-%d")
# Example usage:
# print(nextDay("2023-07-17"))  # Output: "2023-07-18"

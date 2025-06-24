"""
LeetCode 1360. Number of Days Between Two Dates

Given two dates date1 and date2 in the format 'YYYY-MM-DD', return the number of days between them.

Constraints:
- The given dates are valid dates between 1971 and 2100.

Example:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
"""
def daysBetweenDates(date1, date2):
    from datetime import datetime
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d1 - d2).days)

# Example usage:
date1 = "2019-06-29"
date2 = "2019-06-30"
print(daysBetweenDates(date1, date2))  # Output: 1

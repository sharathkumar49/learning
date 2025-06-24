"""
1118. Number of Days in a Month

Given a year and a month, return the number of days in that month.

Constraints:
- 1900 <= year <= 2100
- 1 <= month <= 12

Example:
Input: year = 1992, month = 7
Output: 31
"""
def numberOfDays(year: int, month: int) -> int:
    import calendar
    return calendar.monthrange(year, month)[1]

# Example usage:
year = 1992
month = 7
print(numberOfDays(year, month))  # Output: 31

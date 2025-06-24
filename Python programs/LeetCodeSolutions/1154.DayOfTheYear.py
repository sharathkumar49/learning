"""
1154. Day of the Year

Given a string date representing a Gregorian calendar date in the format YYYY-MM-DD, return the day number of the year.

Constraints:
- date.length == 10
- date[4] == date[7] == '-'
- 1900 <= year <= 2019
- 1 <= month <= 12
- 1 <= day <= 31

Example:
Input: date = "2019-01-09"
Output: 9

"""
def dayOfYear(date):
    from datetime import datetime
    dt = datetime.strptime(date, "%Y-%m-%d")
    return dt.timetuple().tm_yday

# Example usage
if __name__ == "__main__":
    print(dayOfYear("2019-01-09"))  # Output: 9

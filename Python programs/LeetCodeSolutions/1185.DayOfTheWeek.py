"""
1185. Day of the Week

Given a date string date in the format YYYY-MM-DD, return the day of the week.

Constraints:
- date is a valid date between 1971-01-01 and 2100-12-31

Example:
Input: date = "2019-01-06"
Output: "Sunday"

"""
def dayOfTheWeek(date):
    import datetime
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    y, m, d = map(int, date.split('-'))
    return days[datetime.date(y, m, d).weekday()]

# Example usage
if __name__ == "__main__":
    print(dayOfTheWeek("2019-01-06"))  # Output: "Sunday"

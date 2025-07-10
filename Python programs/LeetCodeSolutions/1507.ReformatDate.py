"""
LeetCode 1507. Reformat Date

Given a date string in the form "Day Month Year", return the date in the format "YYYY-MM-DD".

Constraints:
- The given dates are valid dates between the years 1900 and 2100.

Example:
Input: date = "20th Oct 2052"
Output: "2052-10-20"
"""
def reformatDate(date):
    months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
    d, m, y = date.split()
    d = d[:-2].zfill(2)
    return f"{y}-{months[m]}-{d}"

# Example usage:
date = "20th Oct 2052"
print(reformatDate(date))  # Output: "2052-10-20"

"""
LeetCode 2303. Calculate Amount Paid in Taxes

Given brackets and income, return the total tax paid.

Example:
Input: brackets = [[3,50],[7,10],[12,25]], income = 10
Output: 2.65000

Constraints:
- 1 <= brackets.length <= 100
- 0 <= income <= 100
"""

def calculateTax(brackets, income):
    res = prev = 0
    for upper, percent in brackets:
        taxable = min(income, upper) - prev
        if taxable > 0:
            res += taxable * percent / 100
        prev = upper
        if income <= upper:
            break
    return res

# Example usage:
# print(calculateTax([[3,50],[7,10],[12,25]], 10))  # Output: 2.65

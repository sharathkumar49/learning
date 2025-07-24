"""
LeetCode 2525. Categorize Box According to Criteria

Given length, width, height, and mass, categorize the box.

Constraints:
- 1 <= length, width, height, mass <= 10^5
"""

def categorizeBox(length, width, height, mass):
    bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or length*width*height >= 10**9
    heavy = mass >= 100
    if bulky and heavy:
        return "Both"
    if bulky:
        return "Bulky"
    if heavy:
        return "Heavy"
    return "Neither"
# Example usage:
# print(categorizeBox(1000,1000,1000,100))  # Output: "Both"

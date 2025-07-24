"""
LeetCode 2739. Total Distance Traveled

Given mainTank and additionalTank, return the total distance traveled.

Constraints:
- 1 <= mainTank, additionalTank <= 100
"""

def distanceTraveled(mainTank, additionalTank):
    res = 0
    while mainTank >= 5:
        res += 5
        mainTank -= 4
        if additionalTank:
            additionalTank -= 1
            mainTank += 1
    res += mainTank
    return res * 10
# Example usage:
# print(distanceTraveled(5, 10))  # Output: 60

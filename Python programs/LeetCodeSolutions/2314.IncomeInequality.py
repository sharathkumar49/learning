"""
LeetCode 2314. Income Inequality

Given incomes, return the Gini coefficient.

Example:
Input: incomes = [10,20,30,40,50]
Output: 0.2667

Constraints:
- 1 <= incomes.length <= 10^5
"""

def giniCoefficient(incomes):
    n = len(incomes)
    incomes.sort()
    total = sum(incomes)
    gini = 0
    for i, income in enumerate(incomes, 1):
        gini += (2*i - n - 1) * income
    return gini / (n * total)

# Example usage:
# print(giniCoefficient([10,20,30,40,50]))  # Output: 0.2667

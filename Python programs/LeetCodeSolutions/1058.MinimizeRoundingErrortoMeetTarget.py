"""
1058. Minimize Rounding Error to Meet Target

Given an array prices of strings representing prices, each price is a decimal number, and a target integer. Return the minimum rounding error to meet the target, or -1 if it is not possible.

Constraints:
- 1 <= prices.length <= 500
- 0 <= price <= 1000
- 0 <= target <= 10^6

Example:
Input: prices = ["0.700","2.800","4.900"], target = 8
Output: 0.30000
"""
from typing import List

def minimizeError(prices: List[str], target: int) -> str:
    import math
    diffs = []
    floor_sum = 0
    for p in prices:
        f = math.floor(float(p))
        c = math.ceil(float(p))
        floor_sum += f
        if f != c:
            diffs.append(float(p) - f)
    need = target - floor_sum
    if need < 0 or need > len(diffs):
        return "-1"
    diffs.sort()
    error = sum(diffs[:need]) + sum(1 - d for d in diffs[need:])
    return f"{error:.5f}"

# Example usage:
prices = ["0.700","2.800","4.900"]
target = 8
print(minimizeError(prices, target))  # Output: 0.30000

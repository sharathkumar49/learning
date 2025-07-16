"""
LeetCode 2469. Convert the Temperature

Given a temperature in Celsius, return the temperature in Kelvin and Fahrenheit.

Constraints:
- 0 <= celsius <= 1000
"""

def convertTemperature(celsius):
    return [celsius+273.15, celsius*1.80+32.00]

# Example usage:
# print(convertTemperature(36.50))  # Output: [309.65,97.70]

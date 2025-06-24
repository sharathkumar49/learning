"""
LeetCode 1344. Angle Between Hands of a Clock

Given hour and minutes, return the smaller angle (in degrees) between the hour and the minute hand.

Constraints:
- 0 <= hour <= 23
- 0 <= minutes <= 59

Example:
Input: hour = 12, minutes = 30
Output: 165
"""
def angleClock(hour, minutes):
    hour = hour % 12
    h_angle = (hour * 30) + (minutes * 0.5)
    m_angle = minutes * 6
    diff = abs(h_angle - m_angle)
    return min(diff, 360 - diff)

# Example usage:
hour = 12
minutes = 30
print(angleClock(hour, minutes))  # Output: 165

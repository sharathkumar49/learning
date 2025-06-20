"""
478. Generate Random Point in a Circle

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Constraints:
- 0 < radius <= 10^8
- -10^7 <= x_center, y_center <= 10^7

Example:
Input: radius = 1.0, x_center = 0.0, y_center = 0.0
Output: [0.06673, -0.3976]
"""

import random

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center
    def randPoint(self) -> list:
        while True:
            x = random.uniform(-self.radius, self.radius)
            y = random.uniform(-self.radius, self.radius)
            if x*x + y*y <= self.radius*self.radius:
                return [self.x + x, self.y + y]

# Example usage:
sol = Solution(1.0, 0.0, 0.0)
print(sol.randPoint())  # Output: e.g. [0.06673, -0.3976]

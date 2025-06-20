# 11. Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Example 2:
# Input: height = [1,1]
# Output: 1
#
# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example usage
height = [1,8,6,2,5,4,8,3,7]
print("Max area:", maxArea(height))  # Output: 49

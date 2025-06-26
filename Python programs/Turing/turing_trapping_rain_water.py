# Turing: Trapping Rain Water
# Given n non-negative integers representing an elevation map, compute how much water it can trap after raining.

def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    res = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            res += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            res += max(0, right_max - height[right])
    return res

if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
    print(trap([4,2,0,3,2,5]))              # Output: 9

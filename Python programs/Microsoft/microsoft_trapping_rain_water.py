# Microsoft: Trapping Rain Water
# Given n non-negative integers representing an elevation map, compute how much water it can trap after raining.

def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

if __name__ == "__main__":
    arr1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(arr1))  # Output: 6
    arr2 = [4,2,0,3,2,5]
    print(trap(arr2))  # Output: 9

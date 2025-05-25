# Microsoft: Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area

if __name__ == "__main__":
    arr1 = [2,1,5,6,2,3]
    print(largest_rectangle_area(arr1))  # Output: 10
    arr2 = [2,4]
    print(largest_rectangle_area(arr2))  # Output: 4
    arr3 = [6,2,5,4,5,1,6]
    print(largest_rectangle_area(arr3))  # Output: 12

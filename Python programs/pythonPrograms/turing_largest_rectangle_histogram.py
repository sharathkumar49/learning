# Turing: Largest Rectangle in Histogram
# Given n non-negative integers representing the histogram's bar height, find the area of largest rectangle in the histogram.

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area

if __name__ == "__main__":
    print(largest_rectangle_area([2,1,5,6,2,3]))  # Output: 10
    print(largest_rectangle_area([2,4]))          # Output: 4

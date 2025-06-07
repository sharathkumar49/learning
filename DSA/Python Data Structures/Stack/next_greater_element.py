
# Problem: Given an array, find the next greater element for each element. 
# Solution: Use a stack to track elements and map their next greater values.

def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)-1, -1, -1): # Traverse from right to left
        # Here, start is len(nums)-1 (the last index), 
        # stop is -1, to go until index 0 since stop value is exclusive
        # step is -1 (to go backwards).
        print("\n\nstack before while loop",stack)
        while stack and stack[-1] <= nums[i]:
            stack.pop()
            print("stack after pop",stack)
        result[i] = stack[-1] if stack else -1
        print("result after while loop", result)
        stack.append(nums[i])
        print("stack after while loop",stack)

    return result

# Test Cases
print(next_greater_element([4, 5, 2, 25]))  # [5, 25, 25, -1]
print(next_greater_element([13, 7, 6, 12]))  # [-1, 12, 12, -1]

# Time Complexity: O(n)



# Problem:
#     Given an array of integers, for each element, find the next greater element to its right in the array. If no such element exists, return -1 for that position.

# Approach:
#     This implementation uses a stack to efficiently find the next greater element for each item in the array in O(n) time.
#     - The array is traversed from right to left (end to start).
#     - For each element, the stack is used to keep track of potential next greater elements.
#     - Elements are popped from the stack if they are less than or equal to the current element, as they cannot be the next greater for the current or any earlier element.
#     - The top of the stack (if any) after popping is the next greater element for the current position.
#     - The current element is then pushed onto the stack to serve as a candidate for elements to its left.

# Functions:
#     next_greater_element(nums: List[int]) -> List[int]:
#         Returns a list where each index contains the next greater element for the corresponding input element, or -1 if none exists.

# Example:
#     Input:  [4, 5, 2, 25]
#     Output: [5, 25, 25, -1]

#     Input:  [13, 7, 6, 12]
#     Output: [-1, 12, 12, -1]

# Test Cases:
#     The script includes test cases that print the result for sample inputs.

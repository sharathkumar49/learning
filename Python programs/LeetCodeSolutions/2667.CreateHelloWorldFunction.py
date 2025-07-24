"""
LeetCode 2667. Create Hello World Function

Implement a function that returns a function which returns "Hello World".

Constraints:
- 1 <= calls.length <= 10^5
"""

def createHelloWorld():
    return lambda *args, **kwargs: "Hello World"
# Example usage:
# f = createHelloWorld()
# print(f())  # Output: Hello World

"""
LeetCode 2629. Function Composition

Implement a function composition utility.

Constraints:
- 1 <= functions.length <= 1000
"""

def compose(functions):
    def composed(x):
        for f in reversed(functions):
            x = f(x)
        return x
    return composed
# Example usage:
# add1 = lambda x: x+1
# mult2 = lambda x: x*2
# composed = compose([add1, mult2])
# print(composed(4))  # Output: 9

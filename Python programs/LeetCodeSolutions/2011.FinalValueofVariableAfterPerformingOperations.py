"""
LeetCode 2011. Final Value of Variable After Performing Operations

Given an array of strings operations, return the final value of x after performing all the operations. x starts at 0.

Example:
Input: operations = ["--X","X++","X++"]
Output: 1

Constraints:
- 1 <= operations.length <= 100
- operations[i] will be either "++X", "X++", "--X", or "X--".
"""

def finalValueAfterOperations(operations):
    x = 0
    for op in operations:
        if '+' in op:
            x += 1
        else:
            x -= 1
    return x

# Example usage:
# print(finalValueAfterOperations(["--X","X++","X++"]))  # Output: 1

"""
1006. Clumsy Factorial

The factorial of a positive integer n is the product of all positive integers less than or equal to n.

We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

We use floor division for the division operation.

Given an integer n, return the clumsy factorial of n.

Example 1:
Input: n = 4
Output: 7
Explanation: 4 * 3 / 2 + 1 = 7

Example 2:
Input: n = 10
Output: 12

Constraints:
- 1 <= n <= 10^4
"""
def clumsy(n: int) -> int:
    stack = [n]
    n -= 1
    index = 0
    while n > 0:
        if index % 4 == 0:
            stack.append(stack.pop() * n)
        elif index % 4 == 1:
            stack.append(int(stack.pop() / n))
        elif index % 4 == 2:
            stack.append(n)
        else:
            stack.append(-n)
        n -= 1
        index += 1
    return sum(stack)

# Example usage
if __name__ == "__main__":
    print(clumsy(4))   # Output: 7
    print(clumsy(10))  # Output: 12

"""
241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

Constraints:
- 1 <= expression.length <= 20
- expression consists of digits and the operator '+', '-', and '*'.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
"""
def diffWaysToCompute(expression):
    if expression.isdigit():
        return [int(expression)]
    res = []
    for i, c in enumerate(expression):
        if c in '+-*':
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            for l in left:
                for r in right:
                    if c == '+':
                        res.append(l + r)
                    elif c == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
    return res

# Example usage:
if __name__ == "__main__":
    print(sorted(diffWaysToCompute("2-1-1")))      # Output: [0,2]
    print(sorted(diffWaysToCompute("2*3-4*5")))    # Output: [-34,-14,-10,-10,10]

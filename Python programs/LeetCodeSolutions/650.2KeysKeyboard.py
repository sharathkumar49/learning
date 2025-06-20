"""
650. 2 Keys Keyboard
Difficulty: Medium

You have a notepad and can only perform two operations: Copy All and Paste. Initially, there is one character 'A' on the notepad. Return the minimum number of steps to get exactly n 'A's on the notepad.

Example 1:
Input: n = 3
Output: 3

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 1000
"""

def minSteps(n):
    res = 0
    d = 2
    while n > 1:
        while n % d == 0:
            res += d
            n //= d
        d += 1
    return res

# Example usage
if __name__ == "__main__":
    print(minSteps(3))  # Output: 3
    print(minSteps(1))  # Output: 1

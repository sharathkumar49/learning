"""
LeetCode 672. Bulb Switcher II

There is a room with n bulbs, numbered from 1 to n, all turned off initially. Four buttons are available to perform the following operations:
1. Flip all the bulbs.
2. Flip bulbs with even numbers.
3. Flip bulbs with odd numbers.
4. Flip bulbs with (3k + 1) numbers, k = 0, 1, 2, ...

Given n and m (number of operations), return the number of different possible statuses of the n bulbs after performing at most m operations.

Example 1:
Input: n = 1, m = 1
Output: 2

Example 2:
Input: n = 2, m = 1
Output: 3

Example 3:
Input: n = 3, m = 1
Output: 4

Constraints:
- 1 <= n <= 1000
- 0 <= m <= 1000
"""
def flipLights(n: int, m: int) -> int:
    if m == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 3 if m == 1 else 4
    return 4 if m == 1 else 7 if m == 2 else 8

# Example usage
if __name__ == "__main__":
    print(flipLights(1, 1))  # Output: 2
    print(flipLights(2, 1))  # Output: 3
    print(flipLights(3, 1))  # Output: 4

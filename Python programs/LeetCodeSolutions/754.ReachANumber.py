"""
LeetCode 754. Reach a Number

You are standing at position 0 on an infinite number line. There is a destination at position target.
On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
Return the minimum number of moves required to reach the target.

Example 1:
Input: target = 2
Output: 3

Example 2:
Input: target = 3
Output: 2

Constraints:
- -10^9 <= target <= 10^9
- target != 0
"""
def reachNumber(target: int) -> int:
    target = abs(target)
    step = 0
    total = 0
    while total < target or (total - target) % 2 != 0:
        step += 1
        total += step
    return step

# Example usage
if __name__ == "__main__":
    print(reachNumber(2))  # Output: 3
    print(reachNumber(3))  # Output: 2

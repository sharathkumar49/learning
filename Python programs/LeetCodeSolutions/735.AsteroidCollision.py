"""
LeetCode 735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive means right, negative means left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]

Example 2:
Input: asteroids = [8,-8]
Output: []

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]

Constraints:
- 2 <= asteroids.length <= 10^4
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0
"""
from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for a in asteroids:
        while stack and a < 0 < stack[-1]:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            break
        else:
            stack.append(a)
    return stack

# Example usage
if __name__ == "__main__":
    print(asteroidCollision([5,10,-5]))  # Output: [5,10]
    print(asteroidCollision([8,-8]))     # Output: []
    print(asteroidCollision([10,2,-5]))  # Output: [10]

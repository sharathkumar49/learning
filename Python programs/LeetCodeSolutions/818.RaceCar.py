"""
818. Race Car

Your car starts at position 0 and speed +1 on an infinite number line. ("A" means accelerate, "R" means reverse.) Given a target, return the length of the shortest sequence of instructions to reach the target.

Example 1:
Input: target = 3
Output: 2

Example 2:
Input: target = 6
Output: 5

Constraints:
- 1 <= target <= 10000
"""
def racecar(target):
    from collections import deque
    queue = deque([(0, 1, 0)])  # position, speed, steps
    visited = set((0, 1))
    while queue:
        pos, speed, steps = queue.popleft()
        if pos == target:
            return steps
        # Accelerate
        next_state = (pos + speed, speed * 2)
        if (next_state[0], next_state[1]) not in visited and 0 <= next_state[0] <= 2 * target:
            visited.add((next_state[0], next_state[1]))
            queue.append((next_state[0], next_state[1], steps + 1))
        # Reverse
        rev_speed = -1 if speed > 0 else 1
        if (pos, rev_speed) not in visited:
            visited.add((pos, rev_speed))
            queue.append((pos, rev_speed, steps + 1))
    return -1

# Example usage:
print(racecar(3))  # Output: 2
print(racecar(6))  # Output: 5

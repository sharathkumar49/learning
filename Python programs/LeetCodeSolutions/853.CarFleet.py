"""
853. Car Fleet

There are n cars going to the same destination. Each car starts at a different position and speed. A car can never pass another car, but it can catch up and form a fleet. Return the number of fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1

Constraints:
- n == position.length == speed.length
- 1 <= n <= 10^4
- 0 < target <= 10^6
- 0 <= position[i] < target
- All the values of position are unique.
- 0 < speed[i] <= 10^6
"""
def carFleet(target, position, speed):
    cars = sorted(zip(position, speed))
    times = [(target - p) / s for p, s in cars][::-1]
    fleets = 0
    cur = 0
    for t in times:
        if t > cur:
            fleets += 1
            cur = t
    return fleets

# Example usage:
print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))  # Output: 3
print(carFleet(10, [3], [3]))  # Output: 1

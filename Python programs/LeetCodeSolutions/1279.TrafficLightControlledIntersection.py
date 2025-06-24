"""
LeetCode 1279. Traffic Light Controlled Intersection

(This problem requires an external TrafficLight API which is not implemented here. The code below is a template for LeetCode submission.)

Design a traffic light system for an intersection. Each car arrives at the intersection and must wait for the green light in its direction. Implement the TrafficLight class with the following methods:
- carArrived(carId, direction, turnGreen, crossCar): Called when a car arrives. Only one car can cross at a time in each direction.

Constraints:
- 1 <= n <= 1000
- 1 <= carId <= 10^9
- direction in [1,2,3,4]

"""
# The TrafficLight API is not implemented here. This is a template for LeetCode submission.
class TrafficLight:
    def __init__(self):
        self.green = 1
        self.lock = False
    def carArrived(self, carId, direction, turnGreen, crossCar):
        if direction != self.green:
            turnGreen()
            self.green = direction
        crossCar()

# Example usage:
# Not executable here as TrafficLight API is not implemented.

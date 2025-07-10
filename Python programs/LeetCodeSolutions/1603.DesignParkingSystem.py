"""
LeetCode 1603. Design Parking System

Design a parking system for a parking lot. Implement the ParkingSystem class:
- ParkingSystem(int big, int medium, int small): Initializes object with the number of slots for each type.
- bool addCar(int carType): Adds a car of carType (1=big, 2=medium, 3=small). Returns true if there is a slot, false otherwise.

Example 1:
Input: ["ParkingSystem","addCar","addCar","addCar","addCar"], [[1,1,0],[1],[2],[3],[1]]
Output: [null,true,true,false,false]

Constraints:
- 0 <= big, medium, small <= 1000
- 1 <= carType <= 3
- At most 2000 calls will be made to addCar.
"""

class ParkingSystem:
    def __init__(self, big, medium, small):
        self.slots = [0, big, medium, small]
    def addCar(self, carType):
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False

# Example usage:
# ps = ParkingSystem(1, 1, 0)
# print(ps.addCar(1))  # True
# print(ps.addCar(2))  # True
# print(ps.addCar(3))  # False
# print(ps.addCar(1))  # False

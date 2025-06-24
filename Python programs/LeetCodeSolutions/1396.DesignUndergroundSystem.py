"""
LeetCode 1396. Design Underground System

Implement the UndergroundSystem class:
- void checkIn(int id, string stationName, int t)
- void checkOut(int id, string stationName, int t)
- double getAverageTime(string startStation, string endStation)

Constraints:
- There will be at most 2 * 10^4 calls in total to checkIn, checkOut, and getAverageTime.
- All strings consist of uppercase, lowercase English letters and digits.
- 1 <= id, t <= 10^6
- There will be at most 10^4 different id values.

Example:
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.getAverageTime("Leyton", "Waterloo") # return 12.0
"""
class UndergroundSystem:
    def __init__(self):
        self.checkins = {}
        self.trips = {}
    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)
    def checkOut(self, id, stationName, t):
        start, startTime = self.checkins.pop(id)
        key = (start, stationName)
        if key not in self.trips:
            self.trips[key] = [0, 0]
        self.trips[key][0] += t - startTime
        self.trips[key][1] += 1
    def getAverageTime(self, startStation, endStation):
        total, count = self.trips[(startStation, endStation)]
        return total / count

# Example usage:
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkOut(45, "Waterloo", 15)
print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))  # Output: 12.0

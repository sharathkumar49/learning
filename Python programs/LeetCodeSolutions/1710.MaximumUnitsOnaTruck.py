"""
LeetCode 1710. Maximum Units on a Truck

You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxes, numberOfUnitsPerBox]. Also given an integer truckSize, the maximum number of boxes that can be put on the truck. Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8

Constraints:
- 1 <= boxTypes.length <= 1000
- 1 <= numberOfBoxes, numberOfUnitsPerBox <= 1000
- 1 <= truckSize <= 10^6
"""

def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: -x[1])
    units = 0
    for num, unit in boxTypes:
        take = min(truckSize, num)
        units += take * unit
        truckSize -= take
        if truckSize == 0:
            break
    return units

# Example usage:
# boxTypes = [[1,3],[2,2],[3,1]]
# truckSize = 4
# print(maximumUnits(boxTypes, truckSize))  # Output: 8

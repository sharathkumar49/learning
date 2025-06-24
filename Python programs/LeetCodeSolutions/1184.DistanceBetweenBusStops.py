"""
1184. Distance Between Bus Stops

Given a circular route with n bus stops and a distance array, return the shortest distance between two bus stops.

Constraints:
- 1 <= n <= 10^4
- distance.length == n
- 0 <= start, destination < n

Example:
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1

"""
def distanceBetweenBusStops(distance, start, destination):
    if start > destination:
        start, destination = destination, start
    total = sum(distance)
    direct = sum(distance[start:destination])
    return min(direct, total - direct)

# Example usage
if __name__ == "__main__":
    print(distanceBetweenBusStops([1,2,3,4], 0, 1))  # Output: 1

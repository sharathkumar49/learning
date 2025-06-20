"""
774. Minimize Max Distance to Gas Station

On a number line, there are n gas stations at positions stations[0], stations[1], ..., stations[n-1]. We add k more gas stations so that the maximum distance between adjacent gas stations is minimized. Return the smallest possible value of this maximum distance. Answers within 10^-6 of the true value will be accepted.

Example 1:
Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.500000

Constraints:
- 10 <= stations.length <= 2000
- 0 <= stations[i] <= 10^8
- stations are sorted in increasing order
- 1 <= k <= 10^6
"""
def minmaxGasDist(stations, k):
    def possible(D):
        count = 0
        for i in range(1, len(stations)):
            count += int((stations[i] - stations[i-1]) / D)
        return count <= k
    left, right = 0, stations[-1] - stations[0]
    while right - left > 1e-6:
        mid = (left + right) / 2
        if possible(mid):
            right = mid
        else:
            left = mid
    return right

# Example usage:
stations = [1,2,3,4,5,6,7,8,9,10]
k = 9
print(f"{minmaxGasDist(stations, k):.6f}")  # Output: 0.500000

"""
LeetCode 1326. Minimum Number of Taps to Open to Water a Garden

There is a one-dimensional garden of length n. There are n+1 taps, each at position i, and ranges[i] is the range of the i-th tap. Return the minimum number of taps to open to water the whole garden, or -1 if impossible.

Constraints:
- 1 <= n <= 10^4
- ranges.length == n + 1
- 0 <= ranges[i] <= 100

Example:
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
"""
def minTaps(n, ranges):
    max_range = [0] * (n+1)
    for i, r in enumerate(ranges):
        left = max(0, i - r)
        right = min(n, i + r)
        max_range[left] = max(max_range[left], right)
    taps = 0
    end = far = 0
    for i in range(n):
        far = max(far, max_range[i])
        if i == end:
            if far <= i:
                return -1
            taps += 1
            end = far
    return taps

# Example usage:
n = 5
ranges = [3,4,1,1,0,0]
print(minTaps(n, ranges))  # Output: 1

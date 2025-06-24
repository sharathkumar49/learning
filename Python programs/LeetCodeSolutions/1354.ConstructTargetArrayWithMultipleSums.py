"""
LeetCode 1354. Construct Target Array With Multiple Sums

Given an array target, return true if it is possible to construct the array from an array of ones by repeatedly replacing an element with the sum of the array.

Constraints:
- 1 <= target.length <= 5 * 10^4
- 1 <= target[i] <= 10^9

Example:
Input: target = [9,3,5]
Output: true
"""
def isPossible(target):
    import heapq
    total = sum(target)
    target = [-x for x in target]
    heapq.heapify(target)
    while True:
        a = -heapq.heappop(target)
        total -= a
        if a == 1 or total == 1:
            return True
        if a < total or total == 0 or a % total == 0:
            return False
        a %= total
        total += a
        heapq.heappush(target, -a)

# Example usage:
target = [9,3,5]
print(isPossible(target))  # Output: True

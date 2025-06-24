"""
1167. Minimum Cost to Connect Sticks

Given an array of positive integers sticks, you can connect any two sticks with a cost equal to their sum. Return the minimum cost to connect all the sticks into one.

Constraints:
- 1 <= sticks.length <= 10^4
- 1 <= sticks[i] <= 10^4

Example:
Input: sticks = [2,4,3]
Output: 14

"""
def connectSticks(sticks):
    import heapq
    heapq.heapify(sticks)
    cost = 0
    while len(sticks) > 1:
        a = heapq.heappop(sticks)
        b = heapq.heappop(sticks)
        cost += a + b
        heapq.heappush(sticks, a + b)
    return cost

# Example usage
if __name__ == "__main__":
    print(connectSticks([2,4,3]))  # Output: 14

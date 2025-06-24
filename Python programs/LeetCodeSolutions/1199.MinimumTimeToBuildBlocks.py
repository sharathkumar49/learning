"""
1199. Minimum Time to Build Blocks

Given n blocks, each with a time to build, and a split operation that doubles the number of workers, return the minimum time to build all blocks.

Constraints:
- 1 <= blocks.length <= 1000
- 1 <= blocks[i] <= 10^5
- 1 <= split <= 100

Example:
Input: blocks = [1,2,3], split = 1
Output: 4

"""
def minBuildTime(blocks, split):
    import heapq
    heapq.heapify(blocks)
    while len(blocks) > 1:
        x = heapq.heappop(blocks)
        y = heapq.heappop(blocks)
        heapq.heappush(blocks, x + split)
        heapq.heappush(blocks, y)
    return blocks[0]

# Example usage
if __name__ == "__main__":
    print(minBuildTime([1,2,3], 1))  # Output: 4

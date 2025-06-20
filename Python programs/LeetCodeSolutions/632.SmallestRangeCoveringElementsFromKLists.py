"""
632. Smallest Range Covering Elements from K Lists
Difficulty: Hard

You are given k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.

Example 1:
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]

Constraints:
1 <= k <= 3500
-10^5 <= nums[i][j] <= 10^5
"""

def smallestRange(nums):
    import heapq
    k = len(nums)
    heap = [(row[0], i, 0) for i, row in enumerate(nums)]
    heapq.heapify(heap)
    max_val = max(row[0] for row in nums)
    res = [-10**5, 10**5]
    while True:
        min_val, i, j = heapq.heappop(heap)
        if max_val - min_val < res[1] - res[0]:
            res = [min_val, max_val]
        if j + 1 == len(nums[i]):
            break
        next_val = nums[i][j+1]
        heapq.heappush(heap, (next_val, i, j+1))
        max_val = max(max_val, next_val)
    return res

# Example usage
if __name__ == "__main__":
    print(smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))  # Output: [20,24]

"""
LeetCode 2163. Minimum Difference in Sums After Removal of Elements

Given an array nums of length 3n, remove n elements from the left and n from the right to minimize the difference between the sum of the left n and right n elements. Return the minimum possible difference.

Example:
Input: nums = [3,1,2,4,5,6]
Output: -1

Constraints:
- 3 <= nums.length <= 3 * 10^5
- nums.length % 3 == 0
- -10^5 <= nums[i] <= 10^5
"""

def minimumDifference(nums):
    import heapq
    n = len(nums)//3
    left = nums[:n]
    right = nums[-n:]
    left_sum = [sum(left)]
    right_sum = [sum(right)]
    maxh = [-x for x in left]
    heapq.heapify(maxh)
    minh = right[:]
    heapq.heapify(minh)
    s = sum(left)
    for i in range(n, 2*n):
        heapq.heappush(maxh, -nums[i])
        s += nums[i] + heapq.heappop(maxh)
        left_sum.append(s)
    s = sum(right)
    for i in range(2*n-1, n-1, -1):
        heapq.heappush(minh, nums[i])
        s += nums[i] - heapq.heappop(minh)
        right_sum.append(s)
    right_sum = right_sum[::-1]
    return min(a-b for a, b in zip(left_sum, right_sum))

# Example usage:
# print(minimumDifference([3,1,2,4,5,6]))  # Output: -1

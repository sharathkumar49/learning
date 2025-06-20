"""
275. H-Index II
https://leetcode.com/problems/h-index-ii/

Given an array of integers citations sorted in ascending order, return the researcher's h-index.

Constraints:
- n == citations.length
- 1 <= n <= 10^5
- 0 <= citations[i] <= 1000

Example 1:
Input: citations = [0,1,3,5,6]
Output: 3

Example 2:
Input: citations = [1,2,100]
Output: 2
"""
def hIndex(citations):
    n = len(citations)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid - 1
    return n - left

# Example usage:
if __name__ == "__main__":
    print(hIndex([0,1,3,5,6]))  # Output: 3
    print(hIndex([1,2,100]))    # Output: 2

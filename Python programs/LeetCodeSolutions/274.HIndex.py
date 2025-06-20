"""
274. H-Index
https://leetcode.com/problems/h-index/

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

Constraints:
- n == citations.length
- 1 <= n <= 5000
- 0 <= citations[i] <= 1000

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3

Example 2:
Input: citations = [1,3,1]
Output: 1
"""
def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h

# Example usage:
if __name__ == "__main__":
    print(hIndex([3,0,6,1,5]))  # Output: 3
    print(hIndex([1,3,1]))      # Output: 1

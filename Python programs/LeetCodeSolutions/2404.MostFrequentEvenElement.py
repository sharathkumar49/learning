"""
LeetCode 2404. Most Frequent Even Element

Given an array, return the most frequent even element.

Constraints:
- 1 <= nums.length <= 10^5
"""

def mostFrequentEven(nums):
    from collections import Counter
    freq = Counter(x for x in nums if x%2==0)
    if not freq:
        return -1
    max_freq = max(freq.values())
    return min(x for x in freq if freq[x]==max_freq)

# Example usage:
# print(mostFrequentEven([0,1,2,2,4,4,1]))  # Output: 2

"""
1090. Largest Values From Labels

You have a set of items, each with a value and a label. Pick up to num_wanted items with the highest values, with at most use_limit items per label. Return the sum of the values of the items chosen.

Constraints:
- 1 <= values.length == labels.length <= 20000
- 0 <= values[i], num_wanted, use_limit <= 20000

Example:
Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
Output: 9
"""
from typing import List
from collections import Counter

def largestValsFromLabels(values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
    items = sorted(zip(values, labels), reverse=True)
    count = Counter()
    res = 0
    for v, l in items:
        if count[l] < use_limit and num_wanted > 0:
            res += v
            count[l] += 1
            num_wanted -= 1
    return res

# Example usage:
values = [5,4,3,2,1]
labels = [1,1,2,2,3]
num_wanted = 3
use_limit = 1
print(largestValsFromLabels(values, labels, num_wanted, use_limit))  # Output: 9

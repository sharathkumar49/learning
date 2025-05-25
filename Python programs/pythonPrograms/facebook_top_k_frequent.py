# Facebook: Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]

if __name__ == "__main__":
    arr1 = [1,1,1,2,2,3]
    print(top_k_frequent(arr1, 2))  # Output: [1,2]
    arr2 = [1]
    print(top_k_frequent(arr2, 1))  # Output: [1]

# Program: Implement a Queue for Sliding Window Median
# Problem: Find the median in every window of size k in an array using two heaps (queue-like behavior).
import heapq
from collections import deque

def median_sliding_window(nums, k):
    import bisect
    window = sorted(nums[:k])
    medians = []
    for i in range(k, len(nums)+1):
        # Median
        if k % 2 == 1:
            medians.append(window[k//2])
        else:
            medians.append((window[k//2-1] + window[k//2]) / 2)
        if i == len(nums):
            break
        # Remove outgoing
        out = nums[i-k]
        idx = bisect.bisect_left(window, out)
        window.pop(idx)
        # Add incoming
        bisect.insort(window, nums[i])
    return medians

if __name__ == '__main__':
    arr = [1,3,-1,-3,5,3,6,7]
    print(median_sliding_window(arr, 3))

# Amazon: Sliding Window Maximum
# Given an array nums and a sliding window size k, return the max in each window.
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

if __name__ == "__main__":
    print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
    print(max_sliding_window([1], 1))                  # Output: [1]

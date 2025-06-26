# Amazon: Kth Largest Element in an Array
# Find the kth largest element in an unsorted array.
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":
    print(find_kth_largest([3,2,1,5,6,4], 2))  # Output: 5
    print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4

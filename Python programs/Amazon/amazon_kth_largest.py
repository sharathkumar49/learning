# Amazon: Find the kth largest element in an array
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("k: "))
    print("Kth largest:", kth_largest(nums, k))

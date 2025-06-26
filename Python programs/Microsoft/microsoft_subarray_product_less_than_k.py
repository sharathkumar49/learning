# Microsoft: Find the Subarray Product Less Than K
# Given an array of positive integers nums and integer k, return the number of (contiguous, non-empty) subarrays where the product of all elements is less than k.

def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    prod = 1
    left = 0
    count = 0
    for right, n in enumerate(nums):
        prod *= n
        while prod >= k:
            prod //= nums[left]
            left += 1
        count += right - left + 1
    return count

if __name__ == "__main__":
    arr1 = [10,5,2,6]
    print(num_subarray_product_less_than_k(arr1, 100))  # Output: 8
    arr2 = [1,2,3]
    print(num_subarray_product_less_than_k(arr2, 0))    # Output: 0

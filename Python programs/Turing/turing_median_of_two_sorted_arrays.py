# Turing: Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays.

def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 1:
        return nums[n//2]
    else:
        return (nums[n//2-1] + nums[n//2]) / 2

if __name__ == "__main__":
    print(find_median_sorted_arrays([1,3], [2]))      # Output: 2
    print(find_median_sorted_arrays([1,2], [3,4]))    # Output: 2.5

# Amazon: Find the Number of Subarrays with Bounded Maximum
# Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

def num_subarray_bounded_max(nums, left, right):
    def count(bound):
        ans = cur = 0
        for n in nums:
            cur = cur + 1 if n <= bound else 0
            ans += cur
        return ans
    return count(right) - count(left - 1)

if __name__ == "__main__":
    print(num_subarray_bounded_max([2,1,4,3], 2, 3))  # Output: 3
    print(num_subarray_bounded_max([2,9,2,5,6], 2, 8))  # Output: 7

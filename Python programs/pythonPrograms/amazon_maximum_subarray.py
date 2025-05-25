# Amazon: Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def max_sub_array(nums):
    max_sum = curr_sum = nums[0]
    for n in nums[1:]:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(max_sub_array([1]))                      # Output: 1
    print(max_sub_array([5,4,-1,7,8]))             # Output: 23

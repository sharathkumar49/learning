# Amazon: Find the Maximum Average Subarray I
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. Return this value.

def find_max_average(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum / k

if __name__ == "__main__":
    print(find_max_average([1,12,-5,-6,50,3], 4))  # Output: 12.75

# Microsoft: Find the maximum sum subarray (Kadane's Algorithm)
def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    for n in nums[1:]:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)
    return max_sum

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Max subarray sum:", max_subarray(nums))

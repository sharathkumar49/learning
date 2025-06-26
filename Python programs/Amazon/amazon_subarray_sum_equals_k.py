# Amazon: Subarray Sum Equals K
def subarray_sum(nums, k):
    from collections import defaultdict
    count = curr_sum = 0
    sums = defaultdict(int)
    sums[0] = 1
    for n in nums:
        curr_sum += n
        count += sums[curr_sum - k]
        sums[curr_sum] += 1
    return count

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Target sum: "))
    print("Count:", subarray_sum(nums, k))

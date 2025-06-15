
# Length of longest subarray of sum less than or equal to k

# given some array of positive integers s, find the length of the longest
# subarray such that the sum of all its values is less than or equal to
# some positive integer k. Each input will always have at least one solution.
# The array is not circular.


# def max_length(s, k):
#     current = []
#     max_len = -1 # returns -1 if there is no subsequence that adds up to k.
#     for i in s:
#         current.append(i)
#         while sum(current) > k: # Shrink the array from the left, until the sum is <= k.
#            current = current[1:]
#         if sum(current) == k:
#             max_len = max(max_len, len(current))
#
#     return max_len


def max_length(s, k):
    # These two mark the start and end of the subarray that `current` used to be.
    subarray_start = 0
    subarray_end = 0

    subarray_sum = 0
    max_len = -1 # returns -1 if there is no subsequence that adds up to k.
    for i in s:
        subarray_sum += i
        subarray_end += 1
        while subarray_sum > k: # Shrink the array from the left, until the sum is <= k.
            subarray_sum -= s[subarray_start]
            subarray_start += 1

        # After the previous while loop, subarray_sum is guaranteed to be
        # smaller than or equal to k.
        max_len = max(max_len, subarray_end - subarray_start)

    return max_len



print(max_length([1,1,3,4], 5))
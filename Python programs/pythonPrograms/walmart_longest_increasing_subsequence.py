# Walmart: Longest Increasing Subsequence
# Given an unsorted array of integers, find the length of longest increasing subsequence.
import bisect

def length_of_lis(nums):
    sub = []
    for x in nums:
        if not sub or x > sub[-1]:
            sub.append(x)
        else:
            idx = bisect.bisect_left(sub, x)
            sub[idx] = x
    return len(sub)

if __name__ == "__main__":
    print(length_of_lis([10,9,2,5,3,7,101,18]))  # Output: 4
    print(length_of_lis([0,1,0,3,2,3]))          # Output: 4

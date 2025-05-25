# Facebook: Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Must run in O(n) time.

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

if __name__ == "__main__":
    arr1 = [100,4,200,1,3,2]
    print(longest_consecutive(arr1))  # Output: 4
    arr2 = [0,3,7,2,5,8,4,6,0,1]
    print(longest_consecutive(arr2))  # Output: 9

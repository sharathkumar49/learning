# Apple: Longest consecutive sequence in an unsorted array
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
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Longest consecutive sequence:", longest_consecutive(nums))

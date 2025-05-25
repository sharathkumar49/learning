# Microsoft: Find the Missing Ranges
# Given a sorted integer array where the range of elements are [lower, upper] inclusive, return the missing ranges.

def find_missing_ranges(nums, lower, upper):
    res = []
    prev = lower - 1
    nums.append(upper + 1)
    for n in nums:
        if n - prev == 2:
            res.append(str(prev + 1))
        elif n - prev > 2:
            res.append(f"{prev + 1}->{n - 1}")
        prev = n
    return res

if __name__ == "__main__":
    arr1 = [0,1,3,50,75]
    print(find_missing_ranges(arr1, 0, 99))  # Output: ['2', '4->49', '51->74', '76->99']
    arr2 = []
    print(find_missing_ranges(arr2, 1, 1))  # Output: ['1']

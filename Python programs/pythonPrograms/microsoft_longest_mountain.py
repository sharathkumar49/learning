# Microsoft: Find the Longest Mountain in Array
# Given an array, return the length of the longest mountain. A mountain is defined as a sequence that strictly increases and then strictly decreases.

def longest_mountain(arr):
    n = len(arr)
    res = 0
    i = 1
    while i < n-1:
        if arr[i-1] < arr[i] > arr[i+1]:
            left = i-1
            right = i+1
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
            while right < n-1 and arr[right] > arr[right+1]:
                right += 1
            res = max(res, right - left + 1)
            i = right
        else:
            i += 1
    return res

if __name__ == "__main__":
    arr1 = [2,1,4,7,3,2,5]
    print(longest_mountain(arr1))  # Output: 5
    arr2 = [2,2,2]
    print(longest_mountain(arr2))  # Output: 0

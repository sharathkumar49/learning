# Microsoft: Subarray with given sum (positive numbers)
def subarray_sum(arr, target):
    left = curr_sum = 0
    for right, num in enumerate(arr):
        curr_sum += num
        while curr_sum > target and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == target:
            return arr[left:right+1]
    return []

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Target sum: "))
    print("Subarray:", subarray_sum(arr, target))

# Find the second largest element in a list
def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n
        elif first > n > second:
            second = n
    return second if second != float('-inf') else None

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Second largest:", second_largest(nums))

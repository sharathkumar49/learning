# Amazon: Find the missing number in a list of 1 to n
def find_missing(nums, n):
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual

if __name__ == "__main__":
    n = int(input("Enter n: "))
    nums = list(map(int, input(f"Enter {n-1} numbers from 1 to {n}: ").split()))
    print("Missing number:", find_missing(nums, n))

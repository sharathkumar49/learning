"""
1207. Unique Number of Occurrences

Given an array arr, return True if the number of occurrences of each value is unique.

Constraints:
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

Example:
Input: arr = [1,2,2,1,1,3]
Output: True

"""
def uniqueOccurrences(arr):
    from collections import Counter
    count = Counter(arr)
    return len(set(count.values())) == len(count)

# Example usage
if __name__ == "__main__":
    print(uniqueOccurrences([1,2,2,1,1,3]))  # Output: True

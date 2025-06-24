"""
1151. Minimum Swaps to Group All 1's Together

Given a binary array data, return the minimum number of swaps required to group all 1's together in any place in the array.

Constraints:
- 1 <= data.length <= 10^5
- data[i] is 0 or 1

Example:
Input: data = [1,0,1,0,1]
Output: 1

"""
def minSwaps(data):
    total_ones = sum(data)
    if total_ones <= 1:
        return 0
    curr = max_ones = sum(data[:total_ones])
    min_swaps = total_ones - max_ones
    for i in range(total_ones, len(data)):
        curr += data[i] - data[i-total_ones]
        min_swaps = min(min_swaps, total_ones - curr)
    return min_swaps

# Example usage
if __name__ == "__main__":
    print(minSwaps([1,0,1,0,1]))  # Output: 1

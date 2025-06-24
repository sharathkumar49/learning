"""
1215. Stepping Numbers

Given two integers low and high, return a sorted list of all stepping numbers in the range [low, high]. A stepping number is an integer where every adjacent digit has an absolute difference of 1.

Constraints:
- 0 <= low <= high <= 2 * 10^9

Example:
Input: low = 0, high = 21
Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]

"""
def countSteppingNumbers(low, high):
    res = []
    from collections import deque
    for i in range(10):
        q = deque([i])
        while q:
            num = q.popleft()
            if num > high:
                continue
            if num >= low:
                res.append(num)
            if num == 0:
                continue
            last = num % 10
            if last > 0:
                q.append(num * 10 + last - 1)
            if last < 9:
                q.append(num * 10 + last + 1)
    return sorted(set(res))

# Example usage
if __name__ == "__main__":
    print(countSteppingNumbers(0, 21))  # Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]

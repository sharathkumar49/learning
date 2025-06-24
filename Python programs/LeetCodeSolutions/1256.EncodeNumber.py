"""
1256. Encode Number

Given a non-negative integer num, return its encoding as a string.

Constraints:
- 0 <= num <= 10^9

Example:
Input: num = 23
Output: "1000"

"""
def encode(num):
    if num == 0:
        return ""
    n = num + 1
    return bin(n)[3:]

# Example usage
if __name__ == "__main__":
    print(encode(23))  # Output: "1000"

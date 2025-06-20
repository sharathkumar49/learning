# 38. Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
#
# Example 1:
# Input: n = 1
# Output: "1"
#
# Example 2:
# Input: n = 4
# Output: "1211"
#
# Constraints:
# 1 <= n <= 30

def countAndSay(n):
    s = "1"
    for _ in range(n-1):
        prev, count, res = s[0], 1, ''
        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                res += str(count) + prev
                prev = c
                count = 1
        res += str(count) + prev
        s = res
    return s

# Example usage
n = 4
print("Count and Say:", countAndSay(n))  # Output: "1211"

"""
LeetCode 1271. Hexspeak

Given a decimal number, convert it to hexadecimal and replace all digits 0 with 'O', 1 with 'I', and check if the result contains only the characters 'A'-'F', 'I', and 'O'. If not, return 'ERROR'.

Constraints:
- 1 <= num <= 10^12

Example:
Input: num = "257"
Output: "IOI"

"""
def toHexspeak(num):
    num = int(num)
    hexstr = hex(num)[2:].upper()
    hexstr = hexstr.replace('0', 'O').replace('1', 'I')
    for c in hexstr:
        if c not in 'ABCDEFIO':
            return 'ERROR'
    return hexstr

# Example usage:
print(toHexspeak("257"))  # Output: IOI
print(toHexspeak("3"))    # Output: ERROR

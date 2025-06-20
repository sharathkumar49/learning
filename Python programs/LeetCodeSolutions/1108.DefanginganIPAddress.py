"""
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

Constraints:
- The given address is a valid IPv4 address.

Example:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""
def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')

# Example usage:
address = "1.1.1.1"
print(defangIPaddr(address))  # Output: "1[.]1[.]1[.]1"

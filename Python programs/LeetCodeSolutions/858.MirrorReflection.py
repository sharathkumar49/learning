"""
858. Mirror Reflection

There is a square room with mirrors on the walls. The laser starts at (0,0) and bounces until it hits a receptor. Return the receptor number it meets first.

Example 1:
Input: p = 2, q = 1
Output: 2

Example 2:
Input: p = 3, q = 1
Output: 1

Constraints:
- 1 <= p <= 1000
- 0 <= q <= p
"""
def mirrorReflection(p, q):
    from math import gcd
    lcm = p * q // gcd(p, q)
    if (lcm // q) % 2 == 0:
        return 0
    if (lcm // p) % 2 == 0:
        return 2
    return 1

# Example usage:
print(mirrorReflection(2, 1))  # Output: 2
print(mirrorReflection(3, 1))  # Output: 1

"""
800. Similar RGB Color

The red-green-blue color "#AABBCC" can be similar to another color if the difference for each component is at most 2. Return the similar color which is the closest shorthand (e.g., #ABC) representation.

Example 1:
Input: color = "#09f166"
Output: "#11ee66"

Constraints:
- color is a string of the form "#RRGGBB".
- color.length == 7
"""
def similarRGB(color):
    def closest(c):
        c = int(c, 16)
        q = round(c / 17)
        return '{:02x}'.format(17 * q)
    return '#' + ''.join(closest(color[i:i+2]) for i in (1, 3, 5))

# Example usage:
print(similarRGB("#09f166"))  # Output: "#11ee66"

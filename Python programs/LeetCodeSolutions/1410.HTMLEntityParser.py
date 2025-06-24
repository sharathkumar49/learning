"""
LeetCode 1410. HTML Entity Parser

Given a string text, replace all HTML entities with the corresponding special characters.

Constraints:
- 1 <= text.length <= 10^5
- The string may contain any possible characters out of all the 256 ASCII characters.

Example:
Input: text = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."
"""
def entityParser(text):
    entities = {
        "&quot;": '"',
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;": "/"
    }
    for k, v in entities.items():
        text = text.replace(k, v)
    return text

# Example usage:
text = "&amp; is an HTML entity but &ambassador; is not."
print(entityParser(text))  # Output: "& is an HTML entity but &ambassador; is not."

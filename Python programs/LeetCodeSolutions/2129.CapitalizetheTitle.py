"""
LeetCode 2129. Capitalize the Title

Given a string title, capitalize it according to the rules.

Example:
Input: title = "capiTalIze tHe titLe"
Output: "Capitalize The Title"

Constraints:
- 1 <= title.length <= 100
- title consists of words separated by a single space.
"""

def capitalizeTitle(title):
    return ' '.join(w.lower() if len(w) <= 2 else w.capitalize() for w in title.split())

# Example usage:
# print(capitalizeTitle("capiTalIze tHe titLe"))  # Output: "Capitalize The Title"

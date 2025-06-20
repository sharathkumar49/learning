"""
LeetCode 744. Find Smallest Letter Greater Than Target

Given a list of sorted characters letters containing only lowercase English letters and a target letter target, return the smallest letter in the list that is larger than target.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"

Constraints:
- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter.
- letters is sorted in non-decreasing order.
- letters contains at least two different characters.
- target is a lowercase English letter.
"""
from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
    left, right = 0, len(letters)
    while left < right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return letters[left % len(letters)]

# Example usage
if __name__ == "__main__":
    print(nextGreatestLetter(["c","f","j"], "a"))  # Output: "c"
    print(nextGreatestLetter(["c","f","j"], "c"))  # Output: "f"
    print(nextGreatestLetter(["c","f","j"], "d"))  # Output: "f"

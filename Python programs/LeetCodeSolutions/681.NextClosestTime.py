"""
LeetCode 681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. You may use the digits as many times as you want.

Return the next closest time in the same format.

Example 1:
Input: time = "19:34"
Output: "19:39"

Example 2:
Input: time = "23:59"
Output: "22:22"

Constraints:
- time.length == 5
- time is a valid time in the format "HH:MM".
- 0 <= HH < 24
- 0 <= MM < 60
"""
def nextClosestTime(time: str) -> str:
    digits = set(time.replace(':', ''))
    h, m = map(int, time.split(':'))
    while True:
        m += 1
        if m == 60:
            m = 0
            h = (h + 1) % 24
        t = f"{h:02d}:{m:02d}"
        if set(t.replace(':', '')).issubset(digits):
            return t

# Example usage
if __name__ == "__main__":
    print(nextClosestTime("19:34"))  # Output: "19:39"
    print(nextClosestTime("23:59"))  # Output: "22:22"

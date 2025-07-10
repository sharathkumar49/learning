"""
LeetCode 1629. Slowest Key

Given a list of keypresses and their release times, return the key of the longest duration. If there are multiple, return the lexicographically largest key.

Example 1:
Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
Output: "c"

Constraints:
- releaseTimes.length == keysPressed.length
- 1 <= releaseTimes.length <= 1000
- 0 <= releaseTimes[i] <= 10^9
- keysPressed consists of lowercase English letters.
"""

def slowestKey(releaseTimes, keysPressed):
    max_dur = releaseTimes[0]
    res = keysPressed[0]
    for i in range(1, len(releaseTimes)):
        dur = releaseTimes[i] - releaseTimes[i-1]
        if dur > max_dur or (dur == max_dur and keysPressed[i] > res):
            max_dur = dur
            res = keysPressed[i]
    return res

# Example usage:
# releaseTimes = [9,29,49,50]
# keysPressed = "cbcd"
# print(slowestKey(releaseTimes, keysPressed))  # Output: "c"

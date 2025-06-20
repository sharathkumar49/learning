"""
649. Dota2 Senate
Difficulty: Medium

In the world of Dota2, there are two parties: the Radiant and the Dire. The Dota2 senate consists of senators from two parties. Each senator can ban one senator from the other party. Return the party that will finally win.

Example 1:
Input: senate = "RD"
Output: "Radiant"

Example 2:
Input: senate = "RDD"
Output: "Dire"

Constraints:
1 <= senate.length <= 10^4
senate[i] is either 'R' or 'D'.
"""

def predictPartyVictory(senate):
    from collections import deque
    n = len(senate)
    radiant = deque(i for i, c in enumerate(senate) if c == 'R')
    dire = deque(i for i, c in enumerate(senate) if c == 'D')
    while radiant and dire:
        r, d = radiant.popleft(), dire.popleft()
        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)
    return 'Radiant' if radiant else 'Dire'

# Example usage
if __name__ == "__main__":
    print(predictPartyVictory("RD"))   # Output: "Radiant"
    print(predictPartyVictory("RDD"))  # Output: "Dire"

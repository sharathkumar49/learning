"""
1229. Meeting Scheduler

Given two people's available time slots and a meeting duration, return the earliest time slot that works for both.

Constraints:
- 1 <= slots1.length, slots2.length <= 10^4
- slots1[i].length == slots2[i].length == 2
- 0 <= slots1[i][0] < slots1[i][1] <= 10^9
- 0 <= slots2[i][0] < slots2[i][1] <= 10^9
- 1 <= duration <= 10^6

Example:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

"""
def minAvailableDuration(slots1, slots2, duration):
    slots1 = [s for s in slots1 if s[1] - s[0] >= duration]
    slots2 = [s for s in slots2 if s[1] - s[0] >= duration]
    slots1.sort()
    slots2.sort()
    i = j = 0
    while i < len(slots1) and j < len(slots2):
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        if end - start >= duration:
            return [start, start + duration]
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    return []

# Example usage
if __name__ == "__main__":
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0,15],[60,70]]
    print(minAvailableDuration(slots1, slots2, 8))  # Output: [60,68]

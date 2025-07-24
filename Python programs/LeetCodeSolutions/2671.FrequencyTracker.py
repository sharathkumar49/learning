"""
LeetCode 2671. Frequency Tracker

Implement a frequency tracker with add, delete, and hasFrequency methods.

Constraints:
- 1 <= calls.length <= 10^5
"""
class FrequencyTracker:
    def __init__(self):
        from collections import Counter
        self.cnt = Counter()
        self.freq = Counter()
    def add(self, number):
        f = self.cnt[number]
        self.cnt[number] += 1
        self.freq[f] -= 1
        self.freq[f+1] += 1
    def deleteOne(self, number):
        f = self.cnt[number]
        if f:
            self.cnt[number] -= 1
            self.freq[f] -= 1
            self.freq[f-1] += 1
    def hasFrequency(self, frequency):
        return self.freq[frequency] > 0
# Example usage:
# ft = FrequencyTracker()
# ft.add(3)
# ft.add(3)
# print(ft.hasFrequency(2))  # Output: True

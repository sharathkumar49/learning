"""
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/

You are given an array of logs. Each log is a space-delimited string of words. Reorder the logs so that all the letter-logs come before any digit-log. Letter-logs are ordered lexicographically by content, then identifier. Digit-logs maintain their relative ordering.

Constraints:
- 1 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- logs[i] consists of lowercase English letters, digits, and spaces.

Example:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

# Example usage
if __name__ == "__main__":
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    print(Solution().reorderLogFiles(logs))
    # Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

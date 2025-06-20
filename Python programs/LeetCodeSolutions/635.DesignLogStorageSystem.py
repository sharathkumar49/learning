"""
635. Design Log Storage System
Difficulty: Medium

Design a log storage system that supports storing logs and retrieving them based on a time range and granularity.
Implement the LogSystem class:
- put(id, timestamp): Stores the log with id and timestamp.
- retrieve(start, end, granularity): Returns the ids of logs whose timestamps are within the range [start, end] with the given granularity.

Example:
Input: ["LogSystem","put","put","put","retrieve","retrieve"]
[[],[1,"2017:01:01:23:59:59"],[2,"2017:01:01:22:59:59"],[3,"2016:01:01:00:00:00"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Year"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"]]
Output: [null,null,null,null,[1,2,3],[2,3]]

Constraints:
1 <= id <= 300
1 <= timestamp.length <= 19
Timestamp format: "YYYY:MM:DD:HH:MM:SS"
"""

class LogSystem:
    def __init__(self):
        self.logs = []
    def put(self, id: int, timestamp: str):
        self.logs.append((timestamp, id))
    def retrieve(self, start: str, end: str, granularity: str):
        idx = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}[granularity]
        s = start[:idx] + '0'*(19-idx)
        e = end[:idx] + '9'*(19-idx)
        return [id for t, id in self.logs if s <= t[:idx] + '0'*(19-idx) <= e]

# Example usage
# log = LogSystem()
# log.put(1, "2017:01:01:23:59:59")
# log.put(2, "2017:01:01:22:59:59")
# log.put(3, "2016:01:01:00:00:00")
# print(log.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"))  # Output: [1,2,3]
# print(log.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"))  # Output: [2,3]

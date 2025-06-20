"""
359. Logger Rate Limiter

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e., a message printed at timestamp t will not be printed again until timestamp t + 10).

Implement the Logger class:
- Logger() Initializes the logger object.
- bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.

Constraints:
- 0 <= timestamp <= 10^9
- Every message will consist of lowercase English letters, and possibly some digits.
- At most 10^4 calls will be made to shouldPrintMessage.
"""
class Logger:
    def __init__(self):
        self.msg_time = {}
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_time or timestamp - self.msg_time[message] >= 10:
            self.msg_time[message] = timestamp
            return True
        return False

# Example usage:
logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))  # Output: True
print(logger.shouldPrintMessage(2, "bar"))  # Output: True
print(logger.shouldPrintMessage(3, "foo"))  # Output: False
print(logger.shouldPrintMessage(11, "foo")) # Output: True

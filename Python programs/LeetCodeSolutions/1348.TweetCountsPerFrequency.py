"""
LeetCode 1348. Tweet Counts Per Frequency

Design a class to record tweet counts and return the number of tweets per frequency (minute, hour, or day) in a given time range.

Constraints:
- 1 <= number of tweets <= 10^4
- 0 <= time <= 10^9
- At most 10^4 calls to recordTweet and getTweetCountsPerFrequency

Example:
# Not executable here as this is a class design problem for LeetCode.
"""
from collections import defaultdict
import bisect
class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)
    def recordTweet(self, tweetName, time):
        bisect.insort(self.tweets[tweetName], time)
    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        interval = {'minute':60, 'hour':3600, 'day':86400}[freq]
        times = self.tweets[tweetName]
        res = []
        for t in range(startTime, endTime+1, interval):
            l = bisect.bisect_left(times, t)
            r = bisect.bisect_left(times, min(t+interval, endTime+1))
            res.append(r-l)
        return res

# Example usage:
# Not executable here as this is a class design problem for LeetCode.

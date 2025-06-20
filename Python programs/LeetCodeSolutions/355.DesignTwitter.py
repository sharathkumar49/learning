"""
355. Design Twitter

Design a simplified version of Twitter.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with id followerId started following the user with id followeeId.
- void unfollow(int followerId, int followeeId) The user with id followerId started unfollowing the user with id followeeId.

Constraints:
- 1 <= userId, tweetId, followerId, followeeId <= 500
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
"""
import heapq
from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.time, tweetId))
        self.time -= 1
    def getNewsFeed(self, userId: int) -> list:
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            for t in list(self.tweets[u])[:10]:
                heapq.heappush(heap, t)
        return [tweetId for _, tweetId in heapq.nsmallest(10, heap)]
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

# Example usage:
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))  # Output: [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))  # Output: [6, 5]
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))  # Output: [5]

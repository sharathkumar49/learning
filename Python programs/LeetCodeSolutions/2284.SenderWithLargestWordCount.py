"""
LeetCode 2284. Sender With Largest Word Count

Given messages and senders, return the sender with the largest word count.

Example:
Input: messages = ["Hello world","Hi there"], senders = ["Alice","Bob"]
Output: "Alice"

Constraints:
- 1 <= messages.length == senders.length <= 10^5
"""

def largestWordCount(messages, senders):
    from collections import defaultdict
    count = defaultdict(int)
    for msg, sender in zip(messages, senders):
        count[sender] += len(msg.split())
    return max(sorted(count), key=lambda x: count[x])

# Example usage:
# print(largestWordCount(["Hello world","Hi there"], ["Alice","Bob"]))  # Output: "Alice"
